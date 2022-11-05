files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def tic_tac_toe_pretty_board(width=3, height=3):
    ttt_files = files[:width]
    ttt_ranks = [str(i) for i in range(1, height + 1)]

    pretty_board_string = '  |'
    rank_str = ''
    fcounter = width - 1
    for tttf in ttt_files:
        rank_str += ' {} |'.format(fcounter)
        pretty_board_string += '  {}  |'.format(tttf)
        fcounter -= 1

    sep_str = '-' * len(pretty_board_string)
    si = 0
    sep_lst = []
    sep_lst[:0] = sep_str
    while si < len(pretty_board_string):
        if pretty_board_string.find('|', si):
            si = pretty_board_string.index('|', si)
            sep_lst[si] = '|'
            si += 1
        else:
            break
    sep_str_mid = ''.join(sep_lst)

    pretty_board_string = sep_str_mid + '\\n' + pretty_board_string

    for tttr in ttt_ranks:
        counter = (width * int(tttr)) - 1
        fcounter = width - 1

        rank_str_tmp = '' + rank_str

        for tttf in ttt_files:
            rank_str_tmp = rank_str_tmp.replace(str(fcounter), ' {' + str(counter) + '} ')
            # rank_str_tmp = rank_str_tmp.replace(str(fcounter), ' X ')
            counter -= 1
            fcounter -= 1
        rank_str_tmp = tttr + ' |' + rank_str_tmp
        if tttr != ttt_ranks[-1]:
            pretty_board_string = sep_str_mid + '\\n' + rank_str_tmp + '\\n' + pretty_board_string
        else:
            pretty_board_string = sep_str + '\\n' + rank_str_tmp + '\\n' + pretty_board_string
    print(f'{pretty_board_string}')


def connect4_pretty_board(width=7, height=6):
    connect4_files = files[:width]
    connect4_ranks = [str(i) for i in range(1, height + 1)]

    pretty_board_string = '  |'
    rank_str = ''
    fcounter = width - 1
    for connect4f in connect4_files:
        rank_str += ' {} |'.format(fcounter)
        pretty_board_string += '  {}  |'.format(connect4f)
        fcounter -= 1

    sep_str = '-' * len(pretty_board_string)
    si = 0
    sep_lst = []
    sep_lst[:0] = sep_str
    while si < len(pretty_board_string):
        if pretty_board_string.find('|', si):
            si = pretty_board_string.index('|', si)
            sep_lst[si] = '|'
            si += 1
        else:
            break
    sep_str_mid = ''.join(sep_lst)

    pretty_board_string = sep_str_mid + '\\n' + pretty_board_string

    for connect4r in connect4_ranks:
        counter = (width * int(connect4r)) - 1
        fcounter = width - 1

        rank_str_tmp = '' + rank_str

        for _ in connect4_files:
            rank_str_tmp = rank_str_tmp.replace(str(fcounter), ' {' + str(counter) + '} ')
            # rank_str_tmp = rank_str_tmp.replace(str(fcounter), ' X ')
            counter -= 1
            fcounter -= 1
        rank_str_tmp = connect4r + ' |' + rank_str_tmp
        if connect4r != connect4_ranks[-1]:
            pretty_board_string = sep_str_mid + '\\n' + rank_str_tmp + '\\n' + pretty_board_string
        else:
            pretty_board_string = sep_str + '\\n' + rank_str_tmp + '\\n' + pretty_board_string
    print(f'{pretty_board_string}')


# tic_tac_toe_pretty_board()
connect4_pretty_board()
