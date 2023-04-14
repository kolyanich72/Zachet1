XO_gamers = {}
game_table =[]
flag_stop = 0
def print_table(game_table):
    """
    печать таблицы игры
    """
    for y_1 in range(0, XO_gamers['tbl_str']):
        for x_1 in range(0, XO_gamers['tbl_col']):
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
    a  = input ('первый - ? \n' )
    b = input('имя второго игрока - ? \n')

    var = input(a + ' играет крестиком-X или ноликом-0? \n')
    if  var in ['x','X','х','Х']:
        XO_gamers['X'] = a
        XO_gamers["0"] = b

    elif var in ['o','O','о','О','0']:
        XO_gamers['X'] = b
        XO_gamers["0"] = a


def Init_Table():
    """
    формируем таблицу для игрым согласно задаваемым параметрам
    число строк/столбцов и количество в стороке символов для победы
    :return: таблица для игры
    """
    print(' размер таблицы игры? \n')
    var_1 = int(input('число строк \n'))
    var_2 = int(input('число столбцов \n'))
    win_flag =  int(input('выиграшная комбинация - число подряд идущих элементов? \n'))

    if min(var_1, var_2) < win_flag:
        win_flag =  min(var_1, var_2)
        print(f'выиграшная комбинация не может быть больше размера поля.\nустановим - { win_flag}' )

    XO_gamers['tbl_str'] = var_1
    XO_gamers['tbl_col'] = var_2
    XO_gamers['win_flag'] = win_flag
    return  [[' '] * (var_1)  for i in range(var_2)]


def get_index(Text, game_table):
    """
    проверка соответствия типов введенных значений
    :param Text:
    :param game_table:
    :return:
    """
    while True:
        a =input(Text)
        try:
            a = int(a)
        except ValueError:
            print("Должно быть целым")
            continue
        return a


def winner(Table, x, y):
    """
    проверка выигрышной комбинации по вертикали, горизонтали, диагоналям
    :param Table:
    :param y:
    :param x:
    :return: флаг- выиграл текущий игрок
    """
    count_vert = 0
    count_horiz = 0
    count_diag1 = 1
    count_diag2 = 1
    win = 0
    new_cell =  Table[x][y]
    print(new_cell)
    """проверка по горизонтали"""
    for y_1 in range(y, XO_gamers['tbl_str']): #проверка по горизонтал1 вперед
        if new_cell == Table[x][y_1]:
            count_horiz += 1
        else:
            break
    if count_horiz >= XO_gamers['win_flag']:
        win = 1
        return win

    if y > 0: #проверка по горизонтал2 назад
        for y_1 in range(y - 1, -1, -1):
            if new_cell == Table[x][y_1]:
                count_horiz += 1
            else:
                break
    if count_horiz >= XO_gamers['win_flag']:
        win = 1
        return win

    """проверка по вертикали"""
    if x < (XO_gamers['tbl_col']): #проверка по верт1 вниз
        for x_1 in range(x, XO_gamers['tbl_col']):
            if new_cell == Table[x_1][y]:
                count_vert += 1
            else:
                break
    if x >= 0:
        for x_1 in range(x - 1, -1, -1):  #проверка по верт2  вверх
            if new_cell == Table[x_1][y]:
                count_vert += 1
            else:
                break
    if count_vert >= XO_gamers['win_flag']:
        win = 1
        return win

# диагонали
    x_1, y_1 = x-1, y-1
    while x_1>=0 and y_1>=0: # слева направо вверх
        if new_cell == Table[x_1][y_1]:
            count_diag1 += 1
            x_1 -= 1
            y_1 -= 1
        else: break
    if count_diag1 >= XO_gamers['win_flag']:
        win = 1
        return win

    x_1, y_1 = x+1, y+1
    while x_1 < XO_gamers['tbl_col'] and y_1 < XO_gamers['tbl_str']: #слева направо вниз
        if new_cell == Table[x_1][y_1]:
            count_diag1 += 1
            x_1 += 1
            y_1 += 1
        else: break

    if count_diag1 >= XO_gamers['win_flag']:
        win = 1
        return win

    x_1, y_1 = x+1, y-1
    while x_1<XO_gamers['tbl_col'] and y_1>=0: # cправа налево вверх
        if new_cell == Table[x_1][y_1]:
            count_diag2 += 1
            x_1 += 1
            y_1 -= 1
        else: break

    if count_diag2 >= XO_gamers['win_flag']:
        win = 1
        return win

    x_1, y_1 = x-1, y+1
    while x_1>= 0 and y_1< XO_gamers['tbl_str']: #cправа налево вниз
        if new_cell == Table[x_1][y_1]:
            count_diag2 += 1
            x_1 -= 1
            y_1 += 1
        else: break
    if count_diag2 >= XO_gamers['win_flag']:
        win = 1
    return win


def cntrl_cell(game_table):
    """
    ввод и проверка значений строки и столбца
    :param game_table:
    :return:
    """
    while True:
        str_ = int(get_index(f"введите индекс строки от 1  до {XO_gamers['tbl_str']}\n", game_table))-1
        col = int(get_index(f"введите индекс столбца от 1  до {XO_gamers['tbl_col']}\n", game_table))-1

        if col > XO_gamers['tbl_col'] or str_ > XO_gamers['tbl_str']:
            print("вне диапазона")
            continue
        elif game_table[col][str_] in ['X', "0"]:
            print("клетка занята")
            continue
        return (col, str_)


print('начнем')
starter_()
game_table = Init_Table()
print_table(game_table)

while flag_stop != (XO_gamers['tbl_str'] * XO_gamers['tbl_col']) :
    znak = "0" if (flag_stop % 2 != 0) else 'X'
    gamer = XO_gamers["0"] if (flag_stop % 2 != 0) else XO_gamers['X']
    print(f"играет {gamer}")
    col, st = cntrl_cell(game_table)
    game_table[col][st] = znak
    print_table(game_table)
    flag_win = winner(game_table,col, st)
    if flag_win == 1:
        break
    flag_stop += 1

if flag_win == 1:
    print(f"победил {XO_gamers[znak]}")
else: print("Ничья")
