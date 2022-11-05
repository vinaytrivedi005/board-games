files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def tic_tac_toe_index_to_square(width=3, height=3):
    ttt_files = files[:width]
    ttt_ranks = [i for i in range(1, height+1)]
    index = 0

    square_to_index = dict()
    index_to_square = dict()
    for tttr in ttt_ranks:
        for tttf in ttt_files:
            square = tttf + str(tttr)
            square_to_index[square] = index
            index_to_square[str(index)] = square
            index += 1

    return square_to_index, index_to_square


def connect4_index_to_square(width=7, height=6):
    connect4_files = files[:width]
    connect4_ranks = [i for i in range(1, height+1)]
    index = 0

    square_to_index = dict()
    index_to_square = dict()
    for connect4r in connect4_ranks:
        for connect4f in connect4_files:
            square = connect4f + str(connect4r)
            square_to_index[square] = index
            index_to_square[str(index)] = square
            index += 1

    return square_to_index, index_to_square


s2i, i2s = tic_tac_toe_index_to_square()
s2i, i2s = connect4_index_to_square()

print(s2i)
print(i2s)
