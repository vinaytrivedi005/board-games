import os
import logging
from pathlib import Path

import numpy as np
import tensorflow as tf
from tensorflow.python.keras import models, Sequential
from tensorflow.python.keras.layers import Lambda, Convolution2D, Flatten, Dense, Activation, Dropout

from src.boards.board import Board
from src.evaluators.evaluator import Evaluator

logger = logging.getLogger(__name__)
log = logger.log


class TicTacToeNNEvaluator(Evaluator):

    def __init__(self, model_path=None):
        self.__model_path = model_path
        self.__load_model()

    def evaluate(self, board: Board) -> int:
        binary_board = board.get_binary_board('X')
        score = self.predict(binary_board)
        return score

    def __load_model(self):
        if self.__model_path is not None:
            if os.path.exists(self.__model_path) and Path(self.__model_path).is_file():
                self.__model = models.load_model(self.__model_path, custom_objects=None, compile=True)

        self.__create_model()

    def __create_model(self):
        """
                creates a convolution neural network model for position estimation based on game
                :return: model
                """
        model = Sequential()

        # Pre-processing data
        model.add(Lambda(lambda x: 0.1 if x == 0 else x, input_shape=(3, 3, 2)))

        # Layer 1: convolution layer, input 3 x 3 x 2, output 3 x 3 x 16
        model.add(Convolution2D(128, (3, 3), padding='same', activation="relu",
                                kernel_regularizer=tf.keras.regularizers.l2(l=0.01)))
        # Layer 2: convolution layer, input 3 x 3 x 16, output 3 x 3 x 24
        model.add(Convolution2D(128, (3, 3), padding='same', activation="relu",
                                kernel_regularizer=tf.keras.regularizers.l2(l=0.01)))
        # Layer 3: convolution layer, input 3 x 3 x 24, output 3 x 3 x 32
        model.add(Convolution2D(128, (3, 3), padding='same', activation="relu",
                                kernel_regularizer=tf.keras.regularizers.l2(l=0.01)))
        # Layer 4: convolution layer, input 3 x 3 x 32, output 3 x 3 x 40
        model.add(Convolution2D(64, (3, 3), padding='same', activation="relu",
                                kernel_regularizer=tf.keras.regularizers.l2(l=0.01)))

        model.add(Flatten())

        model.add(Dense(128))
        model.add(Activation("relu"))
        model.add(Dropout(0.2))

        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse', metrics=['accuracy', 'mae'])

        self.__model = model

    def predict(self, binary_board):
        binary_board = np.expand_dims(binary_board, axis=0)
        return self.__model.predict(binary_board)

    def train(self, X, y):
        log(logging.INFO, f"X: {X} \n y: {y}")
        self.__model.fit(X, y, validation_split=0.0, shuffle=True, epochs=10, verbose=0)

        models.save_model(self.__model, self.__model_path, overwrite=True, include_optimizer=True)
