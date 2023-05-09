"""
Material module for Metamaterial Analysis Code (MAC). It represents a single material.
"""
from typing import Any
from MetamaterialAnalysisCode.classes.MACTable import MACTable

class MACMaterial:
    """
    Material class for Metamaterial Analysis Code (MAC). It represents a single material.

    Attributes:
        ID: material ID
        StressStrain: stress-strain curve of the material
        Type: type of the material (Supported: MATS1)
        NonLinearity: type of non-linearity of the material (LINEAR, PLASTIC, NLELAST)
        YieldStress: Stress at the yield point in the strain-stress curve of the material
    """

    def __init__(self, id_: int, type_: str, stressstrain: MACTable = None, nonlinearity: str = "", yieldstress: float = 0):
        """
        Constructor for MACMaterial class
        """
        self.__id = id_
        self.__stressstrain = stressstrain
        self.__type = type_
        self.__nonlinearity = nonlinearity
        self.__yieldstress = yieldstress

    @property
    def ID(self):
        return self.__id

    @property
    def StressStrain(self) -> MACTable:
        return self.__stressstrain

    @property
    def Type(self) -> str:
        return self.__type

    @property
    def NonLinearity(self) -> str:
        return self.__nonlinearity

    @property
    def YieldStress(self) -> float:
        return self.__yieldstress

    # Method to print a node. It uses the 8 characters format of Optistruct.
    def __str__(self):

        match self.Type:

            case "MATS1":

                idspaces = " " * (8 - len(str(self.ID)))
                stressspaces = " " * (8 - len(str(self.__stressstrain.ID)))
                nonlinearityspaces = " " * (8 - len(self.NonLinearity))

                return f"MATS1   {self.ID}{idspaces}{self.__stressstrain.ID}{stressspaces}{self.NonLinearity}" + \
                       f"{nonlinearityspaces}\n" + "\n" + " " * 8 + f"{self.YieldStress}\n"


def set_material(**kwargs: dict[str: Any]) -> MACMaterial:
    """
    Function to set a material as MACMaterial object. The function use the kwargs dictionary. The supported type of
    materials are:
        - MATS1: set_material(id=int, type="MATS1", stressstrain=MACTable, nonlinearity="NLELAST"|"PLASTIC  ", yieldstress=float)
    """
    if kwargs["type"] == "MATS1":

        stressstrain = kwargs["stressstrain"]
        type_ = kwargs["type"]
        nonlinearity = kwargs["nonlinearity"]
        yieldstress = kwargs["yieldstress"]
        id = kwargs["id"]
        material = MACMaterial(id, type_, stressstrain, nonlinearity, yieldstress)

        return material

    else:
        raise ValueError("The material type is not supported by the MACMaterial class.")