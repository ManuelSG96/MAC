# Tests para probar el código de análisis de metamateriales
import math
import os
from time import time
import MetamaterialAnalysisCode as MAC

start = time()

tabla_strainstress1 = MAC.set_table(id=20, data=[(0, 0), (0.01, 0.01), (0.02, 0.02), (0.03, 0.03), (0.04, 0.04)])

material1 = MAC.set_material(id=1, type="MATS1", stressstrain=tabla_strainstress1, nonlinearity="PLASTIC",
                             yieldstress=0.02)

material2 = MAC.set_material(id=2, type="MAT1", e=70000, nu=0.3)

beam2 = MAC.set_property(id=2, type="PBEAM", material=[material2], area=2000, i1=0.0001, i2=1, i12=1, j=1)

beam1 = MAC.set_property(id=1, type="PBEAML", material=[material2], section="ROD", dim1=1.0)

cellstructure1 = MAC.set_structure(type="Auxetic", djoint=5.3, dstar=-0.3, heightstar=0.3, hcapas=3,
                                   hprisma=15, stepx=10, stepy=10, nelem=4)


modelo1 = MAC.set_model(modeldimensions=(150, 300, 70), cellstructure=cellstructure1, cellmaterial=[material2],
                        cellproperty=[beam1])

try:
    os.remove(r"C:\Users\manum\Desktop\TFM\test1.fem")
except FileNotFoundError:
    pass

modelo1.write_fem(r"C:\Users\manum\Desktop\TFM\test1.fem")


for i in (1,2,3,4):
    maxz = 40
    minz = 1
    for nodo in modelo1.NodeDict.values():
        if nodo.Coords[2] > maxz:
            maxz = nodo.Coords[2]
        elif nodo.Coords[2] < minz:
            minz = nodo.Coords[2]

    # ESTO ELIMINA LOS ELEMENTOS Y NODOS DE LAS CAPAS SUPERIOR E INFERIOR ##################################################

    elementtodel = set()
    nodetodel = set()
    for elementkey in modelo1.ElementDict.keys():
        for node in modelo1.ElementDict[elementkey].Nodes:
            if node.Coords[2] < (minz+0.1) or node.Coords[2] > (maxz-0.1):
                nodetodel.add(node.ID)
                elementtodel.add(elementkey)

    for elementkey in elementtodel:
        del modelo1.ElementDict[elementkey]

    for nodekey in nodetodel:
        del modelo1.NodeDict[nodekey]
    ########################################################################################################################

nodespc = [nodo for nodo in modelo1.NodeDict.values() if nodo.Coords[2] <= (minz + 0.1)]
nodesdisp = [nodo for nodo in modelo1.NodeDict.values() if nodo.Coords[2] >= (maxz - 0.1)]

miny = 10.
maxy = 1.
for nodo in modelo1.NodeDict.values():
    if nodo.Coords[1] > maxy:
        maxy = nodo.Coords[1]
    elif nodo.Coords[1] < miny:
        miny = nodo.Coords[1]

avgz = (minz + maxz)/2
avgy = (miny + maxy)/2

for node in modelo1.NodeDict.values():
    # aux = (node.Coords[0], node.Coords[1], node.Coords[2] + avgz*math.cos((node.Coords[1]-avgy)/avgy))
    aux = (node.Coords[0],
           node.Coords[1],
           node.Coords[2] + avgz/2*(((node.Coords[1]-avgy)/avgy)**4 + avgz/4*((node.Coords[1]-avgy)/avgy)**2))
    node.Coords = aux


#force1 = MAC.set_load_case(id=1, type="FORCE", nodes=nodesf, direction=(0., 0., -1.), magnitude=1.0)

enforcedispl1 = MAC.set_load(id=1, type="SPC", nodes=nodesdisp, components=[3], displacement=-0.5, load=True)

constraint1 = MAC.set_constraint(id=2, nodes=nodesdisp, components=[3], displacement=-0.5)

constraint2 = MAC.set_constraint(id=2, nodes=nodespc, components=[1, 2, 3, 4, 5, 6], displacement=0)

subcase1 = MAC.set_subcase(id=1, label="linear", loads=[enforcedispl1], constraints=[constraint1, constraint2])

eigr1 = MAC.set_eigr(id=3, type="EIGRL", numroots=20)

subcase2 = MAC.set_subcase(id=2, label="buckling", loads=[enforcedispl1], constraints=[constraint1, constraint2],
                           eigr=eigr1, stat_sub=subcase1)

analysis1 = MAC.set_analysis(model=modelo1, subcases=[subcase1, subcase2])

analysis1.write_fem(r"C:\Users\manum\Desktop\TFM\test6.fem")

nlparmld1 = MAC.set_nlparmld(id=1, dt=0.1)

nlout1 = MAC.set_nlout(id=2, nint=10)

subcase3 = MAC.set_subcase(id=3, label="nonlinear", loads=[enforcedispl1], constraints=[constraint1, constraint2],
                           nlparmld=nlparmld1, nlout=nlout1)

analysis2 = MAC.set_analysis(model=modelo1, subcases=[subcase3])
analysis2.write_fem(r"C:\Users\manum\Desktop\TFM\test10.fem")

end = time()
print(f"Tiempo de ejecucion: {end - start} s")