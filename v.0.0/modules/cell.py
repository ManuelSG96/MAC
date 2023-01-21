# Aqui se encuentran las clases de celdas que existen

class cell:
    """Main class for cells

    Atributes:
    - type: str: type of the cell
    - id: int: id of the cell
    - nodes: list: list of nodes
    - elements: list: list of elements
    - materials: int: Id of the material

    Methods:
    - init: initialize the cell
    - set_cell: set the atributes of the cell
    - get_cell: get the atributes of the cell
    
    """
    def __init__(self, kind, id, nodes, elements, materials):
        self.kind = kind
        self.id = id
        self.nodes = nodes
        self.elements = elements
        self.materials = materials

    def set_cell(self, type, id, nodes, elements, materials):
        self.type = type
        self.id = id
        self.nodes = nodes
        self.elements = elements
        self.materials = materials
    
    def get_cell(self):
        return self.type, self.id, self.nodes, self.elements, self.materials

    
    