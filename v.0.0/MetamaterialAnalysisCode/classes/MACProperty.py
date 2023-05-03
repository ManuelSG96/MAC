"""
Property module with properties classes for the Metamaterial Analysis Code (MAC). There are one class per type of
property. They all derivative of the base class MACProperty, which is an abstract class.
"""

from abc import ABC, abstractmethod

class MACProperty(ABC):
    """
    Property class for the Metamaterial Analysis Code (MAC). It represents a single property.

    Attributes:
        ID: property ID
        Type: type of the property (PBEAM, PSOLID, etc)
        Material: list of the materials of the property
    """

    @abstractmethod
    def __init__(self, id: int, type: str, material: list):
        """
        Constructor for MACProperty class
        """
        self.__id = id
        self.__type = type
        self.__material = material

    @property
    def ID(self):
        return self.__id

    @property
    def Type(self):
        return self.__type

    @property
    def Material(self):
        return self.__material

class MACBeam(MACProperty):
    """
    Beam property class for the Metamaterial Analysis Code (MAC). It represents a single beam property.

    Attributes:
        Area: area of the beam
        I1: Area moment of inertia of the beam
        I2: Area moment of inertia of the beam
        I12: area product of inertia of the beam
        J: torsional stiffness of the beam
    """

    def __init__(self, id: int, type: str, material: list, area: float, i1: float, i2: float, i12: float, j: float):
        """
        Constructor for MACBeam class
        """
        super().__init__(id, type, material)
        self.__area = area
        self.__i1 = i1
        self.__i2 = i2
        self.__i12 = i12
        self.__j = j

    @property
    def Area(self):
        return self.__area

    @property
    def I1(self):
        return self.__i1

    @property
    def I2(self):
        return self.__i2

    @property
    def I12(self):
        return self.__i12

    @property
    def J(self):
        return self.__j

    # Method to print a node. It uses the 8 characters format of Optistruct.
    def __str__(self):

        idspaces = " " * (8 - len(str(self.ID)))
        materialspaces = " " * (8 - len(str(self.__material[0])))
        area = ":.5f".format(self.Area)[:8]
        inertia1 = ":.5f".format(self.I1)[:8]
        inertia2 = ":.5f".format(self.I2)[:8]
        inertia12 = ":.5f".format(self.I12)[:8]
        torsion = ":.5f".format(self.J)[:8]

        return f"PBEAM   {self.ID}{idspaces}{self.__material[0]}{materialspaces}{area}{inertia1}{inertia2}" + \
               f"{inertia12}{torsion}"
