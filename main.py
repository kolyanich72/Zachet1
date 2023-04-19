XO_GAMERS = {}
flag_stop = 0


def print_table(game_table):
    """
    печать таблицы игры
    """
    for y_1 in range(0, XO_GAMERS['tbl_str']):
        for x_1 in range(0, XO_GAMERS['tbl_col']):
            print('|' + game_table[x_1][y_1], end='')
        print('|')


def starter_():
    """
    формируем список имен игроков
    закрепляем за игроками символ для игры
    по умолчанию первый играет- Х
    :return: значения записываются в словарь
    """
    print('имена игроков? \n')
    a = input('первый - ? \n')
    b = input('имя второго игрока - ? \n')

    var = input(a + ' играет крестиком-X или ноликом-0? \n')
    if var in ['x', 'X', 'х', 'Х']:
        XO_GAMERS['X'] = a
        XO_GAMERS["0"] = b

    elif var in ['o', 'O', 'о', 'О', '0']:
        XO_GAMERS['X'] = b
        XO_GAMERS["0"] = a


def init_table():
    """
    формируем таблицу для игрым согласно задаваемым параметрам
    число строк/столбцов и количество в стороке символов для победы
    :return: таблица для игры
    """
    print(' размер таблицы игры? \n')
    var_1 = int(input('число строк \n'))
    var_2 = int(input('число столбцов \n'))
    win_flag = int(input('выиграшная комбинация - число подряд идущих элементов? \n'))

    if min(var_1, var_2) < win_flag:
        win_flag = min(var_1, var_2)
        print(f'выиграшная комбинация не может быть больше размера поля.\nустановим - { win_flag}')

    XO_GAMERS['tbl_str'] = var_1
    XO_GAMERS['tbl_col'] = var_2
    XO_GAMERS['win_flag'] = win_flag
    return [[' '] * var_1 for i in range(var_2)]


def get_index(text):
    """
    проверка соответствия типов введенных значений
    :param text:
    :return:
    """
    while True:
        a = input(text)
        try:
            a = int(a)
        except ValueError:
            print("Должно быть целым")
            continue
        return a


def winner_h(table_, x, y):
    """
    проверка выигрышной комбинации по вертикали, горизонтали, диагоналям
    :param table_:
    :param y:
    :param x:
    :return: флаг- выиграл текущий игрок
    """
    count_horiz = 0
    win = 0
    new_cell = table_[x][y]
    """проверка по горизонтали"""
    for y_1 in range(XO_GAMERS['tbl_str']):
        if new_cell == table_[x][y_1]:
            count_horiz += 1
            if count_horiz >= XO_GAMERS['win_flag']:
                win = 1
                return win
        else:
            count_horiz = 0
    return win


def winner_g(table_, x, y):
    count_vert = 0
    win = 0
    new_cell = table_[x][y]
    """проверка по вертикали"""
    for x_1 in range(XO_GAMERS['tbl_col']):
        if new_cell == table_[x_1][y]:
            count_vert += 1
            if count_vert >= XO_GAMERS['win_flag']:
                win = 1
                return win
        else:
            count_vert = 0
    return win


def winner_d_l_r(table_, x, y):
    # диагонали
    count_diag1 = 1
    win = 0
    new_cell = table_[x][y]
    x_1, y_1 = x-1, y-1
    while x_1 >= 0 and y_1 >= 0:  # слева направо вверх
        if new_cell == table_[x_1][y_1]:
            count_diag1 += 1
            x_1 -= 1
            y_1 -= 1
        else:
            break
    if count_diag1 >= XO_GAMERS['win_flag']:
        win = 1
        return win

    x_1, y_1 = x+1, y+1
    while x_1 < XO_GAMERS['tbl_col'] and y_1 < XO_GAMERS['tbl_str']:  # слева направо вниз
        if new_cell == table_[x_1][y_1]:
            count_diag1 += 1
            x_1 += 1
            y_1 += 1
        else:
            break

    if count_diag1 >= XO_GAMERS['win_flag']:
        win = 1
    return win


def winner_d_r_l(table_, x, y):
    # диагонали cправа налево
    count_diag2 = 1
    win = 0
    new_cell = table_[x][y]

    x_1, y_1 = x+1, y-1
    while x_1 < XO_GAMERS['tbl_col'] and y_1 >= 0:  # cправа налево вверх
        if new_cell == table_[x_1][y_1]:
            count_diag2 += 1
            x_1 += 1
            y_1 -= 1
        else:
            break
    if count_diag2 >= XO_GAMERS['win_flag']:
        win = 1
        return win

    x_1, y_1 = x-1, y+1
    while x_1 >= 0 and y_1 < XO_GAMERS['tbl_str']:  # cправа налево вниз
        if new_cell == table_[x_1][y_1]:
            count_diag2 += 1
            x_1 -= 1
            y_1 += 1
        else:
            break
    if count_diag2 >= XO_GAMERS['win_flag']:
        win = 1
    return win


def cntrl_cell(game_table, znak1):
    """
    ввод и проверка значений строки и столбца
    :param game_table:
    :return: x,y,win - введеные координаты, признак окончания по победе игрока
    """
    while True:
        y = int(get_index(f"введите индекс строки от 1  до {XO_GAMERS['tbl_str']}\n"))-1
        x = int(get_index(f"введите индекс столбца от 1  до {XO_GAMERS['tbl_col']}\n"))-1
        if x > XO_GAMERS['tbl_col']-1 or y > XO_GAMERS['tbl_str']-1:
            print("вне диапазона")
            continue
        elif game_table[x][y] in ['X', "0"]:
            print("клетка занята")
            continue

        game_table[x][y] = znak1
        win = winner_h(game_table, x, y)  # проверка на выигрышную комбинацию по очередно по 4м направлениям
        if win == 0:
            win = winner_g(game_table, x, y)
            if win == 0:
                win = winner_d_r_l(game_table, x, y)
                if win == 0:
                    win = winner_d_l_r(game_table, x, y)
        return win


print('начнем')
starter_()
game_table = init_table()
print_table(game_table)
flag_win = 0
while flag_stop != (XO_GAMERS['tbl_str'] * XO_GAMERS['tbl_col']):
    znak = "0" if (flag_stop % 2 != 0) else 'X'
    gamer = XO_GAMERS["0"] if (flag_stop % 2 != 0) else XO_GAMERS['X']
    print(f"играет {gamer}")
    flag_win = cntrl_cell(game_table, znak)
    print_table(game_table)
    if flag_win != 0:
        break
    flag_stop += 1

if flag_win == 1:
    print(f"победил {XO_GAMERS[znak]}")
else:
    print("Ничья")
