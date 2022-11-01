import os
import json


class Properties:
    __properties = None
    __PROPERTY_FILE_PATH = 'resources/properties.json'

    def __init__(self):
        raise NotImplementedError('{} class cannot be instantiated'. format(type(self).__name__))

    @staticmethod
    def __read():
        if Properties.__properties is not None:
            return

        if not os.path.exists(Properties.__PROPERTY_FILE_PATH):
            raise FileNotFoundError('property file not available on path: {}'.format(Properties.__PROPERTY_FILE_PATH))

        with open(Properties.__PROPERTY_FILE_PATH, 'r') as f:
            Properties.__properties = dict(json.load(f))

    @staticmethod
    def get(key):
        Properties.__read()

        return Properties.__properties.get(key)
