from matplotlib import pyplot as plt
from typing import Final
from colorama import Fore, Style
from enum import Enum
import math
from sympy import Matrix
import numpy as np
import sympy as s


SPACE_LIM = 20
default_values = np.linspace(-SPACE_LIM, SPACE_LIM, 200)

v1: Matrix = Matrix([[1], [3]])
v2: Matrix = Matrix([[8], [-1]])
v3: Matrix = Matrix([[5], [2]])

styleList = ["-D", "-.o", "-.D", "-.", "--", "-"]


class Color(Enum):
    red = "indianred"
    orange = "darkorange"
    green = "Green"
    brown = "sienna"
    blue = "Blue"
    pink = "orchid"
    black = "Black"


class System:
    A: Matrix
    mainVect: Matrix
    vectors: [Matrix]
    color: Color
    xStyle: str
    yStyle: str
    plotName: str
    values: np.ndarray

    def __init__(self, A, mainVect, vectors: [Matrix] = None, color: Color = Color.red, xStyle="-", yStyle="--",
                 plotName: str = None, values: np.ndarray = default_values):
        self.A = A
        self.mainVect = mainVect
        self.vectors = vectors
        self.color = color
        self.xStyle = xStyle
        self.yStyle = yStyle
        self.plotName = plotName
        self.values = values

    def generateVectors(self):
        self.vectors = []
        for t in self.values:
            self.vectors.append(s.exp(self.A * t) * self.mainVect)

    def printInfo(self, b: bool = True):
        print("Вектор - " + str(self.mainVect.tolist()))

        if b:
            return

        printEigenValues(self.A)


def drawColoredPlots(systems: [System], plotName: str, showVect: bool = False, limit: bool = False):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot()

    for i in range(len(systems)):
        system: System = systems[i]
        l = len(system.vectors)
        pX = [system.vectors[i][0, 0] for i in range(l)]
        pY = [system.vectors[i][1, 0] for i in range(l)]

        legend = ""
        if system.plotName is not None:
            legend += system.plotName + " "

        legend += "V" + str(i)

        if not showVect:
            ax.plot(system.values, pX, system.xStyle, color=system.color.value, label=legend + " & x0")
            ax.plot(system.values, pY, system.yStyle, color=system.color.value, label=legend + " & x1")

            ax.plot([0, system.mainVect[0, 0] * SPACE_LIM], [0, system.mainVect[1, 0] * SPACE_LIM],
                    ":", color=system.color.value, label=legend)
        else:
            ax.plot(pX, pY, "-", color=system.color.value, label=legend + " x(t)")

    ax.set_xlim([0, SPACE_LIM])

    if limit:
        ax.set_xlim([-SPACE_LIM, SPACE_LIM])
        ax.set_ylim([-SPACE_LIM, SPACE_LIM])

    ax.legend()
    ax.grid()

    ax.set_title("Задание №" + str(plotName))
    plt.show()


# def getP(matrix: Matrix) -> Matrix:
#     l = int(len(matrix)**0.5)
#
#     res: Matrix = s.eye(l)
#     vectors = getEigenvectors(matrix)
#
#     for i in range(l):
#         v = vectors[i]
#         for j in range(l):
#             res[j, i] = v[j]
#
#     return res


def getEigenvectors(m: Matrix) -> [Matrix]:
    array = m.eigenvects()
    sym_eigenvectors: [Matrix] = []
    for tup in array:
        for v in tup[2]:
            numbers = list(v)
            if not hasComplex(numbers):
                sym_eigenvectors.append(v)
    return sym_eigenvectors


def printEigenValues(m: Matrix):
    print("Матрица:")
    for row in m.tolist():
        print("\t" + str(row))

    vals = m.eigenvects()
    pos = 1
    print("Спектральный анализ:")
    for value in vals:
        print(str(pos) + ") Собственное число - " + str(round(value[0], 2)) + ". Собственные векторы:")
        for v in value[2]:
            print("\t" + str(list(v)))
        pos += 1


def printCoreAndRange(m: Matrix):
    nullspace = m.nullspace()
    span = m.columnspace()

    print("\nЯдро матрицы:")
    if len(nullspace) == 0:
        print("\t{0}")
    else:
        for v in nullspace:
            print("\t" + str(list(v)))

    print("\nОбраз матрицы:")
    if len(span) == 0:
        print("\t{0}")
    else:
        for v in span:
            print("\t" + str(list(v)))


def hasComplex(array: []) -> bool:
    for n in array:
        if "I" in str(n):
            return True
    return False


def showAll(m: Matrix, text: str, lock):
    vs = [v1, v2, v3]
    cs = [Color.red, Color.orange, Color.green]

    print("\n" + Fore.BLUE + "Задание №" + text + Fore.RESET)
    array = []

    printEigenValues(m)

    for i in range(len(vs)):
        system: System = System(m, mainVect=vs[i], color=cs[i])
        system.generateVectors()
        system.printInfo()
        array.append(system)

    fIm = False
    sIm = False

    if lock == 1:
        fIm = True
    elif lock == 2:
        sIm = True
    elif lock == 3:
        fIm = True
        sIm = True

    drawColoredPlots(array, text, False, fIm)
    drawColoredPlots(array, text, True, sIm)
