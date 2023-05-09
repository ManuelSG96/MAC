# Tests para probar el código de análisis de metamateriales
import os
import MetamaterialAnalysisCode as MAC

tabla_strainstress = MAC.set_table(id=20, data=[(0, 0), (0.01, 0.01), (0.02, 0.02), (0.03, 0.03), (0.04, 0.04)])
material2 = MAC.set_material(id=1, type="MATS1", stressstrain=tabla_strainstress, nonlinearity="PLASTIC",
                             yieldstress=0.02)
beam2 = MAC.set_property(id=1, type="PBEAM", material=[material2], area=2000, i1=0.0001, i2=1, i12=1, j=1)
cellstructure2 = MAC.set_structure(type="Auxetic", djoint=0.3, dstar=0.3, heightstar=0.4, hcapas=3,
                                   hprisma=2, stepx=1, stepy=1)
modelo2 = MAC.set_model(modeldimensions=(10, 10, 10), cellstructure=cellstructure2, cellmaterial=[material2],
                        cellproperty=[beam2])
try:
    os.remove(r"C:\Users\manum\Desktop\TFM\test1.fem")
except FileNotFoundError:
    pass

modelo2.write_fem(r"C:\Users\manum\Desktop\TFM\test1.fem")

#analysis2 = MAC.set_analysis(model=modelo2, analysis="normal_modes", subcase=1, method="LANB", nmode=10)