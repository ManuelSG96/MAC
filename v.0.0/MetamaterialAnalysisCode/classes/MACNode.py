"""
Node module for the Metamaterial Analysis Code (MAC). It represents a single grid.
"""


class MACNode:
    """
    Node class for the Metamaterial Analysis Code (MAC). It represents a single grid.

    Attributes:
        ID: node ID
        Coords: Coordinates of the node
    """

    def __init__(self, id_: int, coords: tuple[float]):
        """
        Constructor for MACNode class
        """
        self.__id = id_
        self.__coords = coords

    @property
    def ID(self):
        return self.__id

    @property
    def Coords(self):
        return self.__coords

    # Method to compare two nodes. It returns True if the nodes are the same (they have the same coordinates),
    # False otherwise.
    def __eq__(self, other) -> bool:
        if isinstance(other, MACNode):
            return self.Coords == other.Coords
        else:
            return False

    # Method to print a node. It uses the 8 characters format of Optistruct.
    def __str__(self):

        idspaces = " " * (8 - len(str(self.ID)))
        systemspaces = " " * 8

        # 8 characters for each coordinate. It uses scientific notation with 3 decimal places.
        x = "{:.2e}".format(self.Coords[0])
        if self.Coords[0] >= 0:
            x = "+" + x
        x = x[:-2] + x[-1:]

        y = "{:.2e}".format(self.Coords[1])
        if self.Coords[1] >= 0:
            y = "+" + y
        y = y[:-2] + y[-1:]

        z = "{:.2e}".format(self.Coords[2])
        if self.Coords[2] >= 0:
            z = "+" + z
        z = z[:-2] + z[-1:]

        return f"GRID    {self.ID}{idspaces}{systemspaces}{x}{y}{z}"
