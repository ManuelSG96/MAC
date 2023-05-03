"""
Cell Structure module for Metamaterial Analysis Code(MAC). It represents the structure.
"""

from MACNode import MACNode
from MACElement import MACElement
from MACGlobals import NODES_SET, NODES_COUNT, ELEMENTS_SET, ELEMENTS_COUNT

class MACAuxetic:
    """
    Auxetic Structure class for Metamaterial Analysis Code (MAC). It represents the auxetic structure.

    Attributes:
        Djoint: distance between the auxiliary nodes (M1, M2) and the horizontal central plane
        Dstar: distance between the first group of nodes (B1,...,B6) and the center of the cell
        Heightstar: distance between the second group of nodes (S1,...,S6) and the horizontal central plane
    """

    def __init__(self, v1: float, v2: float, stepx: float = 1, stepy: float = 1):
        """
        Constructor for MACAuxetic class
        """
        self.__v1 = v1
        self.__v2 = v2
        self.__stepx = stepx
        self.__stepy = stepy

        self.__djoint = self.__stepy * self.__v1
        self.__dstar = self.__stepx * self.__v2
        self.__heightstar = self.__stepy * (1 - self.__v1)

    @property
    def Djoint(self) -> float:
        return self.__djoint

    @property
    def Dstar(self) -> float:
        return self.__dstar

    @property
    def Heightstar(self) -> float:
        return self.__heightstar

    def build(self, cellcenter: tuple[float]):

        x = cellcenter[0]
        y = cellcenter[1]
        z = cellcenter[2] + self.__djoint
        aux = MACNode(NODES_COUNT, (x,y,z))
        if aux not in NODES_SET:
            NODES_SET.add(aux)
            NODES_COUNT += 1
            M1 = aux

        M2 =
        B1 =
        B2 =
        B3 =
        B4 =
        B5 =
        B6 =
        S1 =
        S2 =
        S3 =
        S4 =
        S5 =
        S6 =
        nodes = (M1, M2, B1, B2, B3, B4, B5, B6, S1, S2, S3, S4, S5, S6)

        # Vars: S1-B2, B2-S6, S6-B1, B1-S5, S5-B6, B6-S4, S4-B5, B5-S3, S3-B4, B4-S2, S2-B3 y B3-S1

        S1_B2 = MACElement(1, "VAR", (S1, B2), self.__djoint, self.__dstar, self.__heightstar)

