#!/usr/bin/env python

import os
import sys

MODULE_ROOT = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, MODULE_ROOT)

from class7.utils import get_fib_num


# For exercise 1
class Shape(object):
    def __init__(self, area=0, num_of_sides=0):
        self.area = self._get_area()
        self.num_of_sides = num_of_sides

    def _get_area(self):
        msg = 'This shape must have a method to get area.'
        raise NotImplementedError(msg)


class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
        super(Rectangle, self).__init__(area=area, num_of_sides=4)

    def _get_area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length_of_side=0):
        super(Square, self).__init__(
            length=length_of_side, width=length_of_side)


def exercise2():
    with open('fib_nums.txt', 'w') as my_file:
        for n in range(1, 31):
            fib_num = get_fib_num(n)
            my_file.write('{}\n'.format(fib_num))


if __name__ == '__main__':
    exercise2()

