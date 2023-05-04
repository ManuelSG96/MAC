"""
Cell Structure module for Metamaterial Analysis Code(MAC). It represents the structure.
"""

from MACNode import MACNode
from MACElement import MACElement
from MACGlobals import NODES_SET, ELEMENTS_SET


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

    def build(self, cellcenter: tuple[float], matid: int, propid: int, vvector: tuple)\
            -> tuple[tuple[MACNode], tuple[MACElement]]:

        # M1
        x = cellcenter[0]
        y = cellcenter[1]
        z = cellcenter[2] + self.__djoint
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                M1 = existingnode
                del aux
                break
            else:
                M1 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # M2
        x = cellcenter[0]
        y = cellcenter[1]
        z = cellcenter[2] - self.__djoint
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                M2 = existingnode
                del aux
                break
            else:
                M2 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # S1
        x1 = cellcenter[0] + self.__stepx
        y1 = cellcenter[1]
        z1 = cellcenter[2] + self.__heightstar
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                S1 = existingnode
                del aux
                break
            else:
                S1 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # S2
        x2 = cellcenter[0] + self.__stepx/2
        y2 = cellcenter[1] - self.__stepy
        z2 = cellcenter[2] - self.__heightstar
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                S2 = existingnode
                del aux
                break
            else:
                S2 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # S3
        x3 = cellcenter[0] - self.__stepx/2
        y3 = cellcenter[1] - self.__stepy
        z3 = cellcenter[2] + self.__heightstar
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                S3 = existingnode
                del aux
                break
            else:
                S3 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # S4
        x4 = cellcenter[0] - self.__stepx
        y4 = cellcenter[1]
        z4 = cellcenter[2] - self.__heightstar
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                S4 = existingnode
                del aux
                break
            else:
                S4 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # S5
        x5 = cellcenter[0] - self.__stepx/2
        y5 = cellcenter[1] + self.__stepy
        z5 = cellcenter[2] + self.__heightstar
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                S5 = existingnode
                del aux
                break
            else:
                S5 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # S6
        x6 = cellcenter[0] + self.__stepx/2
        y6 = cellcenter[1] + self.__stepy
        z6 = cellcenter[2] - self.__heightstar
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                S6 = existingnode
                del aux
                break
            else:
                S6 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # B1
        x = (2 - self.__dstar)*cellcenter[0] - (1-self.__dstar)*(x6+x5)/2
        y = (2 - self.__dstar)*cellcenter[1] - (1-self.__dstar)*(y6+y5)/2
        z = (2 - self.__dstar)*cellcenter[2] - (1-self.__dstar)*(z6+z5)/2
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                B1 = existingnode
                del aux
                break
            else:
                B1 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # B2
        x = (2 - self.__dstar)*cellcenter[0] - (1-self.__dstar)*(x1+x6)/2
        y = (2 - self.__dstar)*cellcenter[1] - (1-self.__dstar)*(y1+y6)/2
        z = (2 - self.__dstar)*cellcenter[2] - (1-self.__dstar)*(z1+z6)/2
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                B2 = existingnode
                del aux
                break
            else:
                B2 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # B3
        x = (2 - self.__dstar)*cellcenter[0] - (1-self.__dstar)*(x1+x2)/2
        y = (2 - self.__dstar)*cellcenter[1] - (1-self.__dstar)*(y1+y2)/2
        z = (2 - self.__dstar)*cellcenter[2] - (1-self.__dstar)*(z1+z2)/2
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                B3 = existingnode
                del aux
                break
            else:
                B3 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # B4
        x = (2 - self.__dstar)*cellcenter[0] - (1-self.__dstar)*(x2+x3)/2
        y = (2 - self.__dstar)*cellcenter[1] - (1-self.__dstar)*(y2+y3)/2
        z = (2 - self.__dstar)*cellcenter[2] - (1-self.__dstar)*(z2+z3)/2
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                B4 = existingnode
                del aux
                break
            else:
                B4 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # B5
        x = (2 - self.__dstar)*cellcenter[0] - (1-self.__dstar)*(x4+x3)/2
        y = (2 - self.__dstar)*cellcenter[1] - (1-self.__dstar)*(y4+y3)/2
        z = (2 - self.__dstar)*cellcenter[2] - (1-self.__dstar)*(z4+z3)/2
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                B5 = existingnode
                del aux
                break
            else:
                B5 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        # B6
        x = (2 - self.__dstar)*cellcenter[0] - (1-self.__dstar)*(x4+x5)/2
        y = (2 - self.__dstar)*cellcenter[1] - (1-self.__dstar)*(y4+y5)/2
        z = (2 - self.__dstar)*cellcenter[2] - (1-self.__dstar)*(z4+z5)/2
        aux = MACNode(len(NODES_SET) + 1, (x, y, z))
        for existingnode in NODES_SET:
            if existingnode == aux:
                B6 = existingnode
                del aux
                break
            else:
                B6 = MACNode(len(NODES_SET) + 1, (x, y, z))
                NODES_SET.add(aux)
                del aux

        nodes = (M1, M2, B1, B2, B3, B4, B5, B6, S1, S2, S3, S4, S5, S6)

        # CBEAMS that connect the nodes and build the cell
        elemcount = len(ELEMENTS_SET)

        S1_B2 = MACElement(elemcount + 1, "CBEAM", [S1, B2], [matid], [propid], vvector)
        ELEMENTS_SET.add(S1_B2)

        B2_S6 = MACElement(elemcount + 2, "CBEAM", [B2, S6], [matid], [propid], vvector)
        ELEMENTS_SET.add(B2_S6)

        S6_B1 = MACElement(elemcount + 3, "CBEAM", [S6, B1], [matid], [propid], vvector)
        ELEMENTS_SET.add(S6_B1)

        B1_S5 = MACElement(elemcount + 4, "CBEAM", [B1, S5], [matid], [propid], vvector)
        ELEMENTS_SET.add(B1_S5)

        S5_B6 = MACElement(elemcount + 5, "CBEAM", [S5, B6], [matid], [propid], vvector)
        ELEMENTS_SET.add(S5_B6)

        B6_S4 = MACElement(elemcount + 6, "CBEAM", [B6, S4], [matid], [propid], vvector)
        ELEMENTS_SET.add(B6_S4)

        S4_B5 = MACElement(elemcount + 7, "CBEAM", [S4, B5], [matid], [propid], vvector)
        ELEMENTS_SET.add(S4_B5)

        B5_S3 = MACElement(elemcount + 8, "CBEAM", [B5, S3], [matid], [propid], vvector)
        ELEMENTS_SET.add(B5_S3)

        S3_B4 = MACElement(elemcount + 9, "CBEAM", [S3, B4], [matid], [propid], vvector)
        ELEMENTS_SET.add(S3_B4)

        B4_S2 = MACElement(elemcount + 10, "CBEAM", [B4, S2], [matid], [propid], vvector)
        ELEMENTS_SET.add(B4_S2)

        S2_B3 = MACElement(elemcount + 11, "CBEAM", [S2, B3], [matid], [propid], vvector)
        ELEMENTS_SET.add(S2_B3)

        B3_S1 = MACElement(elemcount + 12, "CBEAM", [B3, S1], [matid], [propid], vvector)
        ELEMENTS_SET.add(B3_S1)

        M1_S2 = MACElement(elemcount + 13, "CBEAM", [M1, S2], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_S2)

        M1_S4 = MACElement(elemcount + 14, "CBEAM", [M1, S4], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_S4)

        M1_S6 = MACElement(elemcount + 15, "CBEAM", [M1, S6], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_S6)

        M2_S1 = MACElement(elemcount + 16, "CBEAM", [M2, S1], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_S1)

        M2_S3 = MACElement(elemcount + 17, "CBEAM", [M2, S3], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_S3)

        M2_S5 = MACElement(elemcount + 18, "CBEAM", [M2, S5], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_S5)

        M1_B1 = MACElement(elemcount + 19, "CBEAM", [M1, B1], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_B1)

        M1_B2 = MACElement(elemcount + 20, "CBEAM", [M1, B2], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_B2)

        M1_B3 = MACElement(elemcount + 21, "CBEAM", [M1, B3], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_B3)

        M1_B4 = MACElement(elemcount + 22, "CBEAM", [M1, B4], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_B4)

        M1_B5 = MACElement(elemcount + 23, "CBEAM", [M1, B5], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_B5)

        M1_B6 = MACElement(elemcount + 24, "CBEAM", [M1, B6], [matid], [propid], vvector)
        ELEMENTS_SET.add(M1_B6)

        M2_B1 = MACElement(elemcount + 25, "CBEAM", [M2, B1], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_B1)

        M2_B2 = MACElement(elemcount + 26, "CBEAM", [M2, B2], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_B2)

        M2_B3 = MACElement(elemcount + 27, "CBEAM", [M2, B3], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_B3)

        M2_B4 = MACElement(elemcount + 28, "CBEAM", [M2, B4], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_B4)

        M2_B5 = MACElement(elemcount + 29, "CBEAM", [M2, B5], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_B5)

        M2_B6 = MACElement(elemcount + 30, "CBEAM", [M2, B6], [matid], [propid], vvector)
        ELEMENTS_SET.add(M2_B6)

        elements = [S1_B2, B2_S6, S6_B1, B1_S5, S5_B6, B6_S4, S4_B5, B5_S3, S3_B4, B4_S2,
                    S2_B3, B3_S1, M1_S2, M1_S4, M1_S6, M2_S1, M2_S3, M2_S5, M1_B1, M1_B2,
                    M1_B3, M1_B4, M1_B5, M1_B6, M2_B1, M2_B2, M2_B3, M2_B4, M2_B5, M2_B6]


        return nodes, elements
