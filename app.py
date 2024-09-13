"""
Поле 3х3, пользователь вводит координаты своего хода, компьютер делает
случайный ход, кто играет крестиками выбирается случайно, если кто-то
выиграл – это выводится на экран.
"""

import random

ALL_SPACES = list("123456789")  # ключи для словаря игры.
X = "X"
O = "O"
EMPTY = " "  # константы для заполнения игрового поля


def main():
    """Запускает игру крестики-нолики"""
    flag = True
    print("Добро пожаловать в крестики-нолики!")
    while flag:
        game_board = get_blanc_board()  # создаем словарь для игры
        current_player = random.choice([X, O])
        if current_player == X:
            print("Вы играете крестиками 'X'")
            computer_player = O
        else:
            print("Вы играете ноликами 'O'")
            computer_player = X

        while True:
            print(get_board_str(game_board))  # Отображаем поле на экране

            # спрашиваем игрока про его ход пока он не введет 1-9:
            move = None
            while not is_valid_space(game_board, move):
                print('Выберите ваш ход (1-9), для выхода введите "q"')
                move = input("> ")
                if move.lower() == "q":
                    print("Пока!")
                    exit()
            update_board(game_board, move, current_player)  # делаем ход

            # проверяем закончилась ли игра:
            if is_winner(game_board, current_player):  # проверяем победу
                print(get_board_str(game_board))
                print("Вы победили!")
                break
            elif is_board_full(game_board):  # проверяем ничью
                print(get_board_str(game_board))
                print("Ничья!")
                break
            # делаем ход компьютером
            move = None
            while not is_valid_space(game_board, move):
                move = random.choice(ALL_SPACES)
            update_board(game_board, move, computer_player)
            # проверяем закончилась ли игра:
            if is_winner(game_board, computer_player):  # проверяем победу
                print(get_board_str(game_board))
                print("Компьютер победил!")
                break
            elif is_board_full(game_board):  # проверяем ничью
                print(get_board_str(game_board))
                print("Ничья!")
                break
        print("Спасибо за игру!")
        another_game = input("Чтобы сыграть еще раз введите: y > ")
        if another_game.lower() != "y":
            flag = False
            print("Пока!")


def get_blanc_board():
    """Создаем пустое поле"""
    board = {}
    for space in ALL_SPACES:
        board[space] = EMPTY  # Все поля сначала пустые
    return board


def get_board_str(board):
    """Создаем игровое поле"""
    return f"""
        {board['1']}|{board['2']}|{board['3']}   1 2 3
        -+-+-
        {board['4']}|{board['5']}|{board['6']}   4 5 6
        -+-+-
        {board['7']}|{board['8']}|{board['9']}   7 8 9"""


def is_valid_space(board, space):
    """
    Возвращает True если ход правильный и место для хода свободно
    """
    return space in ALL_SPACES and board[space] == EMPTY


def is_winner(board, player):
    """Возвращает True если игрок победитель на текущем поле"""
    b, p = board, player  # укоротил имена чтобы не загромождать пространство
    # Проверяем на победу 3 вертикали, 3 горизонтали и две диагонали
    # fmt: off
    return ((b['1'] == b['2'] == b['3'] == p) or  # верхняя горизонталь
            (b['4'] == b['5'] == b['6'] == p) or  # средняя горизонталь
            (b['7'] == b['8'] == b['9'] == p) or  # нижняя горизонталь
            (b['1'] == b['4'] == b['7'] == p) or  # левая вертикаль
            (b['2'] == b['5'] == b['8'] == p) or  # средняя вертикаль
            (b['3'] == b['6'] == b['9'] == p) or  # правая вертикаль
            (b['3'] == b['5'] == b['7'] == p) or  # / диагональ
            (b['1'] == b['5'] == b['9'] == p))  # \ диагональ
    # fmt: on


def is_board_full(board):
    """Возвращает True если все места на поле заняты"""
    for space in ALL_SPACES:
        if board[space] == EMPTY:
            return False  # Если хоть одно место пустое, возвращает False
    return True  # Все места заняты, возвращает True


def update_board(board, space, player):
    """Отмечает ход на поле"""
    board[space] = player


if __name__ == "__main__":
    main()
