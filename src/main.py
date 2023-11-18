from colorama import Fore, Style
from typing import Final
import sympy as s
from sympy import Matrix
from utils import System
from utils import Color
import utils


def p1_1():
    m: Matrix = Matrix([[-1, 0], [0, -1]])

    utils.showAll(m, "1.1", 3)


def p1_2():
    m: Matrix = Matrix([[1, 3], [0, 1]])

    utils.showAll(m, "1.2", 2)


def p1_3():
    m: Matrix = Matrix([[1, -1], [0, -2]])

    utils.showAll(m, "1.3", 3)


def p1_4():
    m: Matrix = Matrix([[0, 6.5], [-1, -1]])

    utils.showAll(m, "1.4", 3)


def p1_5():
    m: Matrix = Matrix([[1, 6.5], [-1, 0]])

    utils.showAll(m, "1.5", 3)


def p1_6():
    m: Matrix = Matrix([[1/2, 6.5], [-1, -1/2]])

    utils.showAll(m, "1.6", 3)


if __name__ == "__main__":
    p1_6()
