"""
    游戏逻辑控制器，负责处理游戏核心算法．
"""

from model import Location
import random


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾.
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并
        """
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向右移动
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def move_up(self):
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    def move_down(self):
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            方阵转置
        :param sqr_matrix: 二维列表类型的方阵
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def generate_new_number(self):
        """
            生成新数字
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = self.__select_random_number()
        self.__list_empty_location.remove(loc)

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        # 每次统计空位置，都先清空之前的数据，避免影响本次数据．
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        """
            游戏是否结束
        :return: False表示没有结束 True 表示结束
        """
        # 是否具有空位置
        if len(self.__list_empty_location) > 0:
            return False

        # 判断横向有没有相同的元素
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r]) - 1):  # 0 1 2
                if self.__map[r][c] == self.__map[r][c + 1]:
                    return False

        # 判断竖向有没有相同的元素
        for c in range(4):
            for r in range(3):
                if self.__map[r][c] == self.__map[r + 1][c]:
                    return False

        return True


# ---------测试代码---------------


if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move_left()
    # print(controller.map)
    # controller.move_down()
    # print(controller.map)

    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()

    print(controller.map)
