"""
Main module for the Metamaterial Analysis Code (MAC) package. It represents the whole model.
"""

from MACMaterial import MACMaterial
from MACProperty import MACProperty


class MACModel:
    """
    Main class for the Metamaterial Analysis Code (MAC) package. It represents the whole model.

    Attributes:
        ModelDimensions: dimensions of the model
        CellStructure: structure of the cell (BBC, FCC, Auxetic, etc)
        CellSize: size of the cell
        CellMaterial: MACMaterial of the cell
        CellProperty: MACProperty of the cell
    """

    def __init__(self, modeldimensions: tuple[float], cellstructure: str, cellsize: float, cellmaterial: MACMaterial,
                 cellproperty: MACProperty):
        """
        Constructor for MACModel class
        """
        self.__modeldimensions = modeldimensions
        self.__cellstructure = cellstructure
        self.__cellsize = cellsize
        self.__cellmaterial = cellmaterial
        self.__cellproperty = cellproperty

        if self.__cellstructure == "AUXETIC":
            pass

        else:
            print("Cell structure not recognized. Please choose between: AUXETIC")
