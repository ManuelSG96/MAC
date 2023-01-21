import sys
import cell

# Module that writes the .fem file

# Diferent cell types can be selelcted

if cell_type == "BC":
    cell.bc_generator(cell_atributes)
elif cell_type == "BCC":
    cell.bcc_generator(cell_atributes)
elif cell_type == "FCC":
    cell.fcc_generator(cell_atributes)
elif cell_type == "HEX":
    cell.hex_generator(cell_atributes)
elif cell_type == "TET":
    cell.tet_generator(cell_atributes)
elif cell_type == "OCT":
    cell.oct_generator(cell_atributes)
elif cell_type == "AUX":
    cell.aux_generator(cell_atributes)
else:
    print("Cell type not recognized")
    sys.exit("Cell type not recognized")
