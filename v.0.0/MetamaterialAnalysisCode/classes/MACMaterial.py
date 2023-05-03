"""
Material module for Metamaterial Analysis Code (MAC). It represents a single material.
"""

class MACMaterial:
    """
    Material class for Metamaterial Analysis Code (MAC). It represents a single material.

    Attributes:
        ID: material ID
        StressStrain: stress-strain curve of the material
        Type: type of the material (MAT1, MATS1, MAT2, etc)
        NonLinearity: type of non-linearity of the material (LINEAR, PLASTIC, NLELAST)
        YieldStress: Stress at the yield point in the strain-stress curve of the material
    """

    def __init__(self, id_: int, stressstrain: int, type_: str, nonlinearity: str, yieldstress: float = 0):
        """
        Constructor for MACMaterial class
        """
        self.__id = id_
        self.__stressstrain = stressstrain
        self.__type = type_
        if nonlinearity == "PLASTIC":
            self.__nonlinearity = "PLASTIC"
        elif nonlinearity == "NLELAST":
            self.__nonlinearity = "NLELAST"
        elif nonlinearity == "LINEAR":
            self.__nonlinearity = "LINEAR"
        else:
            self.__nonlinearity = ""
        self.__yieldstress = yieldstress

    @property
    def ID(self):
        return self.__id

    @property
    def StressStrain(self) -> list:
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
                stressspaces = " " * (8 - len(str(self.__stressstrain)))
                nonlinearityspaces = " " * (8 - len(self.NonLinearity))

                return f"MATS1   {self.ID}{idspaces}{self.__stressstrain}{stressspaces}{self.NonLineality}" + \
                       f"{nonlinearityspaces}\n" + "\n" + " " * 8 + f"{self.YieldStress}"