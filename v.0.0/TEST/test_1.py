try:
    import sys

    sys.path.insert(0, r'C:\MAC\v.0.0')
    import MetamaterialAnalysisCode as MAC
except ImportError:
    print('Some modules where not found')

modelo1 = MAC.blank_model()
modelo1.ModelDimensions = (1, 1, 1)
modelo1.set_structure("AUXETIC", v1=0.2, v2=0.2)

material2 = MAC.set_material(id=1, type="MATS1", e=1, g=1, nu=0.3, rho=1)
beam2 = MAC.set_property(id=1, type="CBEAM", material=[material2], area=1, i1=1, i2=1, i12=1, j=1)
cellstructure2 = MAC.set_structure(structure="AUXETIC", properties=[beam2], v1=0.2, v2=0.2)
modelo2 = MAC.set_model(modeldimensions=(1, 1, 1), structure=cellstructure2)
modelo2.displ_nodes(nodesafected=20, movepersize=1)
modelo2.del_elements(elementsafected=1)
modelo2.write_fem(r"C:\Users\jose_\Desktop\test_1.fem")

analysis2 = MAC.set_analysis(model=modelo2, analysis="normal_modes", subcase=1, method="LANB", nmode=10)
analysis2.write_fem(r"C:\Users\jose_\Desktop\test_1.fem")