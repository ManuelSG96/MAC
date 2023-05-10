# Tests para probar el código de análisis de metamateriales
import os
from time import time
import MetamaterialAnalysisCode as MAC

tabla_strainstress1 = MAC.set_table(id=20, data=[(0, 0), (0.01, 0.01), (0.02, 0.02), (0.03, 0.03), (0.04, 0.04)])

material1 = MAC.set_material(id=1, type="MATS1", stressstrain=tabla_strainstress1, nonlinearity="PLASTIC",
                             yieldstress=0.02)

material2 = MAC.set_material(id=2, type="MAT1", e=70000, nu=0.3)

beam2 = MAC.set_property(id=2, type="PBEAM", material=[material2], area=2000, i1=0.0001, i2=1, i12=1, j=1)

beam1 = MAC.set_property(id=1, type="PBEAML", material=[material2], section="ROD", dim1=0.05)

cellstructure1 = MAC.set_structure(type="Auxetic", djoint=-0.3, dstar=0.3, heightstar=0.4, hcapas=3,
                                   hprisma=2, stepx=1, stepy=1)

start = time()
modelo1 = MAC.set_model(modeldimensions=(20, 20, 20), cellstructure=cellstructure1, cellmaterial=[material2],
                        cellproperty=[beam1])
end = time()
print(f"Tiempo de ejecucion: {end - start} s")
try:
    os.remove(r"C:\Users\manum\Desktop\TFM\test1.fem")
except FileNotFoundError:
    pass

modelo1.write_fem(r"C:\Users\manum\Desktop\TFM\test1.fem")

#analysis2 = MAC.set_analysis(model=modelo2, analysis="normal_modes", subcase=1, method="LANB", nmode=10)