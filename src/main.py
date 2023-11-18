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
    utils.SPACE_LIM = 10
    m: Matrix = Matrix([[1, 4], [0, 1]])

    utils.showAll(m, "1.2", 3)


def p1_3():
    utils.SPACE_LIM = 20
    m: Matrix = Matrix([[1, -1], [0, -2]])

    utils.showAll(m, "1.3", 3)


def p1_4():
    m: Matrix = Matrix([[0, 13], [-2, -2]])

    utils.showAll(m, "1.4", 3)


def p1_5():
    m: Matrix = Matrix([[2, 13], [-2, 0]])

    utils.showAll(m, "1.5", 3)


def p1_6():
    utils.SPACE_LIM = 10
    m: Matrix = Matrix([[1/2, 6.5], [-1, -1/2]])

    utils.showAll(m, "1.6", 3)


def p3_1_6():
    m1 = Matrix([[-1, 6], [0, -1]])
    utils.showAll(m1, "3.1", 2, True)

    sqrInv2 = 2**(-0.5)
    m2 = Matrix([[-sqrInv2, sqrInv2], [-sqrInv2, -sqrInv2]])
    utils.showAll(m2, "3.2", 3, True)

    m3 = Matrix([[1, 2], [-1, -1]])
    utils.showAll(m3, "3.3", 3, True)

    m4 = Matrix([[sqrInv2, sqrInv2], [-sqrInv2, sqrInv2]])
    utils.showAll(m4, "3.4", 3, True)

    m5 = Matrix([[1, 6], [0, 1]])
    utils.showAll(m5, "3.5", 0, True)

    m6 = Matrix([[-1/8, 5], [0, -1/8]])
    utils.showAll(m6, "3.6", 1, True)


def p3_7_12():
    m1 = Matrix([[1/8, 1/32], [-1, -1/8]])
    utils.showAll(m1, "3.7", 1, True)

    m2 = Matrix([[-1/8, 7], [0, 1/8]])
    utils.showAll(m2, "3.8", 1, True)

    m3 = Matrix([[-2, 5], [0, -2]])
    utils.showAll(m3, "3.9", 0, True)

    m4 = Matrix([[2, 1/32], [-1, -2]])
    utils.showAll(m4, "3.10", 0, True)

    m5 = Matrix([[2, 12], [0, 2]])
    utils.showAll(m5, "3.11", 0, True)

    m6 = Matrix([[1, 1], [-1, -1]])
    utils.showAll(m6, "3.12", 0, True)


def p5():
    m1: Matrix = Matrix([[0, 1], [-7, -3]])
    utils.showAll(m1, "5.1", 3)

    m2: Matrix = Matrix([[0, 1], [-7, 0]])
    utils.showAll(m2, "5.2", 3)

    m3: Matrix = Matrix([[0, 1], [7, 0]])
    utils.showAll(m3, "5.3", 3)

    m1: Matrix = Matrix([[0, 1], [7, -3]])
    utils.showAll(m1, "5.4", 3)


if __name__ == "__main__":
    p5()
