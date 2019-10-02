import numpy as np


class TicTacToe:
    """ Класс для крестиков-ноликов
    """

    def __init__(self, first='x'):
        """
        Args:
            first (str): кто первый ходит
        """

        # словарь, чтобы сделать порядок
        signs = {'x': 1, 'o': -1}
        available_signs = set(signs.keys())

        # получаем второго, кто ходит
        second = available_signs.difference(first).pop()

        # словарь для красивого представления
        self.digits = {1: 'x', -1: 'o'}

        # список порядка
        self.order = [signs[first], signs[second]]

        # сама доска
        self.board = np.zeros([3, 3])

    def _paint_board(self):
        """ Делает красивую доску для вывода
            на доске могут быть 1, -1 и 0 => x, o, ' '

        Returns:
            np.array: доска в представлении на печать
        """

        current_board = self.board.copy().astype(int).astype(str)
        current_board[current_board == '1'] = self.digits[1]
        current_board[current_board == '-1'] = self.digits[-1]
        current_board[current_board == '0'] = ' '
        return current_board

    def validate_input(self, to_split):
        try:
            self.m, self.n = map(int, to_split.split())
            return True
        except ValueError:
            print('Enter two values, please')
            return False

    def validate_m_n(self, m, n):
        if n > 3 or m > 3:
            print('Size of the board is 3x3, try again')
            return False
        return True

    def play(self):
        """ Главная функция для игры
        """

        # флаг, что кто-то выиграл
        won = False

        # флаг, что ещё есть место на доске
        still_left = np.any(self.board == 0)

        # пока никто не выиграл и есть место
        while not won and still_left:

            # по выбранному порядку
            for player in self.order:

                # флаг, что ходит текущий игрок
                player_turn = True

                # пока ход игрока, принимаем две корректные координаты
                while player_turn and still_left:
                    print(f'\nInput where to place {self.digits[int(player)]}:')
                    entered = input()
                    if not self.validate_input(entered):
                        continue

                    if not self.validate_m_n(self.m, self.n):
                        continue

                    # если место не занято, то заниимаем его знаком текущего игрока
                    if not self.board[self.m, self.n]:
                        self.board[self.m, self.n] = player

                        # проверяем, не выиграл ли он
                        won = player if self._check_win() else False
                        still_left = np.any(self.board == 0)
                        player_turn = False

                    else:
                        print('Already taken, try again')

                # рисуем доску
                print(self._paint_board())
                if won or not still_left:
                    break

        # если никто не выиграл, но места нет, то ничья
        if not still_left:
            print('\nDraw')

        # если выиграл кто-то, выводим
        elif won:
            print(f'\nPlayer {self.digits[int(player)]} wins')

    def _check_win(self):
        """ Проверка на победу

        Returns:
            bool: либо False, если никто не выиграл, либо True
        """

        won = False
        if np.any(self.board.sum(axis=1) == 3.) or np.any(self.board.sum(axis=0) == 3.) or \
                (np.trace(self.board) == 3.) or (np.trace(self.board[::-1]) == 3.):
            won = True
        return won


