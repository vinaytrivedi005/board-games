def tic_tac_toe_winning_positions():
    winning_positions = list()

    for i in range(9):
        if i % 3 == 0:
            winning_positions.append((2 ** i) + (2 ** (i + 1)) + (2 ** (i + 2)))
        if i < 3:
            winning_positions.append((2 ** i) + (2 ** (i + 3)) + (2 ** (i + 6)))
        if i == 0:
            winning_positions.append((2 ** i) + (2 ** (i + 4)) + (2 ** (i + 8)))
        if i == 2:
            winning_positions.append((2 ** i) + (2 ** (i + 2)) + (2 ** (i + 4)))

    return sorted(winning_positions)


def connect4_winning_positions():
    """
    [15, 30, 60, 120, 1920, 3840, 7680, 15360, 245760, 491520, 983040, 1966080, 2113665, 2130440, 4227330, 4260880,
    8454660, 8521760, 16843009, 16909320, 17043520, 31457280, 33686018, 33818640, 62914560, 67372036, 67637280,
    125829120, 134744072, 135274560, 251658240, 270549120, 272696320, 541098240, 545392640, 1082196480, 1090785280,
    2155905152, 2164392960, 2181570560, 4026531840, 4311810304, 4328785920, 8053063680, 8623620608, 8657571840,
    16106127360, 17247241216, 17315143680, 32212254720, 34630287360, 34905128960, 69260574720, 69810257920,
    138521149440, 139620515840, 275955859456, 277042298880, 279241031680, 515396075520, 551911718912, 554084597760,
    1030792151040, 1103823437824, 1108169195520, 2061584302080, 2207646875648, 2216338391040, 4123168604160]
    :return:
    """
    winning_positions = list()

    for i in range(42):
        if i % 7 in [0, 1, 2, 3]:
            winning_positions.append((2 ** i) + (2 ** (i + 1)) + (2 ** (i + 2)) + (2 ** (i + 3)))
        if i < 21:
            winning_positions.append((2 ** i) + (2 ** (i + 7)) + (2 ** (i + 14)) + (2 ** (i + 21)))
        if (i + 24) < 42 and ((i + 3) % 7) > (i % 7):
            winning_positions.append((2 ** i) + (2 ** (i + 8)) + (2 ** (i + 16)) + (2 ** (i + 24)))
        if (i + 18) < 42 and (i - 3) >= 0 and (i % 7) > ((i - 3) % 7):
            winning_positions.append((2 ** i) + (2 ** (i + 6)) + (2 ** (i + 12)) + (2 ** (i + 18)))

    return sorted(winning_positions)


def decimal_to_binary(num):
    b = ''
    negative_flag = False

    if num == 0:
        return str(num)

    if num < 0:
        num = num * -1
        negative_flag = True

    while num > 0:
        b = str(num % 2) + b
        num = num // 2

    if negative_flag:
        b = '-' + b

    return b


# wp = tic_tac_toe_winning_positions()
wp = connect4_winning_positions()
print(len(wp))
print(wp)
for w in wp:
    print(decimal_to_binary(w))
