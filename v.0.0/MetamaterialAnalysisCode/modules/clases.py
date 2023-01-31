# Aqui se encuentran las clases de celdas que existen

class Cell:
    """Main class for cells

    Atributes:
    - type: str: type of the cell
    - id: int: id of the cell
    - nodes: list: list of nodes
    - elements: list: list of elements
    - materials: int: Id of the material
    - Borrar

    Methods:
    - init: initialize the cell
    - set_cell: set the atributes of the cell
    - get_cell: get the atributes of the cell
    
    """
    def __init__(self, kind, id, nodes, elements, materials):
        self.__kind = kind
        self.id = id
        self.nodes = nodes
        self.elements = elements

    def set_cell(self, type, id, nodes, elements, materials):
        self.type = type
        self.id = id
        self.nodes = nodes
        self.elements = elements
    
    def get_cell(self):
        return self.type, self.id, self.nodes, self.elements, self.materials


class Grid:
    """Class for grids

    Atributes:
    - id: int: id of the grid
    - coords: list: list of coordinates

    Methods:
    - init: initialize the grid
    - set_grid: set the atributes of the grid
    - get_grid: get the atributes of the grid
    
    """
    def __init__(self, id, coords):
        self.id = id
        self.coords = coords

    def set_grid(self, id, coords):
        self.id = id
        self.coords = coords
    
    def get_grid(self):
        return self.id, self.coords

class Element:
    """Class for elements

    Atributes:
    - id: int: id of the element
    - name: int:

    Methods:
    - init: initialize the element
    - set_element: set the atributes of the element
    - get_element: get the atributes of the element
    
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def set_element(self, id, name):
        self.id = id
        self.name = name
    
    def get_element(self):
        return self.id, self.name

class Property:
    """Class for properties

    Atributes:
    - id: int: id of the property
    - name: int:

    Methods:
    - init: initialize the property
    - set_property: set the atributes of the property
    - get_property: get the atributes of the property
    
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def set_property(self, id, name):
        self.id = id
        self.name = name
    
    def get_property(self):
        return self.id, self.name

class Material:
    """Class for materials

    Atributes:
    - id: int: id of the material
    - name: int:

    Methods:
    - init: initialize the material
    - set_material: set the atributes of the material
    - get_material: get the atributes of the material
    
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def set_material(self, id, name):
        self.id = id
        self.name = name
    
    def get_material(self):
        return self.id, self.name

class Subcases:
    """Class for subcases

    Atributes:
    - id: int: id of the subcase
    - name: int:

    Methods:
    - init: initialize the subcase
    - set_subcase: set the atributes of the subcase
    - get_subcase: get the atributes of the subcase
    
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def set_subcase(self, id, name):
        self.id = id
        self.name = name
    
    def get_subcase(self):
        return self.id, self.name