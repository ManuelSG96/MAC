"""
Element module for the Metamaterial Analysis Code (MAC). It represents a single element.
"""


class MACElement:
    """
    Element class for the Metamaterial Analysis Code (MAC). It represents a single element.

    Attributes:
        ID: element ID
        Type: type of the element (CBEAM, CQUAD, etc)
        Nodes: list of nodes that compose the element
        Material: list of the materials of the element
        Properties: list of the properties of the element
        Vvector: vector that determines the orientation of the element

    """

    def __init__(self, id_: int, type_: str, nodes: list, material: list, properties: list, vvector: tuple):
        """
        Constructor for MACElement class
        """
        self.__id = id_
        self.__type = type_
        self.__nodes = nodes
        self.__material = material
        self.__properties = properties
        self.__vvector = vvector

    @property
    def ID(self):
        return self.__id

    @property
    def Type(self):
        return self.__type

    @property
    def Nodes(self):
        return self.__nodes

    @property
    def Materials(self):
        return self.__material

    @property
    def Property(self):
        return self.__properties

    @property
    def Vvector(self):
        return self.__vvector

    # Method to print a node. It uses the 8 characters format of Optistruct.
    def __str__(self):

        match self.Type:

            case "CBEAM":

                idspaces = " " * (8 - len(str(self.ID)))
                typespaces = " " * (8 - len(str(self.Type)))
                node0spaces = " " * (8 - len(str(self.Nodes[0])))
                node1spaces = " " * (8 - len(str(self.Nodes[1])))
                vv0spaces = " " * (8 - len(str(self.Vvector[0])))
                vv1spaces = " " * (8 - len(str(self.Vvector[1])))
                vv2spaces = " " * (8 - len(str(self.Vvector[2])))

                return f"CBEAM   {self.ID}{idspaces}{self.Type}{typespaces}{self.Nodes[0]}{node0spaces}" + \
                       f"{self.Nodes[1]}{node1spaces}{self.Vvector[0]}{vv0spaces}{self.Vvector[1]}{vv1spaces}" + \
                       f"{self.Vvector[2]}{vv2spaces}"

            case "CQUAD":

                return "CQUAD is not yet implemented"
