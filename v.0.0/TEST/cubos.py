import MetamaterialAnalysisCode as mac

# Unidades en milimetros

enf_displ = -5  # Desplazamiento forzado

# Definicion de materiales
aluminio = mac.set_material(id=1, type="MAT1", e=70000, nu=0.3, rho=0.0027)
acero = mac.set_material(id=2, type="MAT1", e=200000, nu=0.3, rho=0.0079)
titanio = mac.set_material(id=3, type="MAT1", e=110000, nu=0.3, rho=0.00423)
mat = ["Al", "St", "Ti"]
count = 0

# Definicion de propiedades
beam_al = mac.set_property(id=1, type="PBEAML", material=[aluminio], section="ROD", dim1=0.5)
beam_ac = mac.set_property(id=2, type="PBEAML", material=[acero], section="ROD", dim1=0.5)
beam_ti = mac.set_property(id=3, type="PBEAML", material=[titanio], section="ROD", dim1=0.5)
vigas = [beam_al, beam_ac, beam_ti]

# Parametros de la celda
v1list = [round(-0.8+i*0.2, 1) for i in range(9)]
v2list = [round(0. + i*0.25, 2) for i in range(3)]
hcapas = 7
dstar = 0.3
hprisma = 10
stepx = 10
stepy = 10

# Dimensiones del modelo:
dim = (100, 100, 100)

for viga in vigas:

    # Definicion de la estructura de la celda
    for v1 in v1list:
        for v2 in v2list:

            # Calculo de parametros geometricos a partir de v1 y v2
            djoint = v1*hcapas/2
            heightstar = v2*djoint

            # Definiciónde la estructura de la celda
            cellstructure = mac.set_structure(type="Auxetic", djoint=djoint, dstar=dstar, heightstar=heightstar, hcapas=hcapas,
                                              hprisma=hprisma, stepx=stepx, stepy=stepy, nelem=4)

            # Definicion del modelo
            modelo = mac.set_model(modeldimensions=dim, cellstructure=cellstructure,
                                   cellmaterial=[viga.Material[0]], cellproperty=[viga])

            minz = 5. - round(abs(djoint), 2)
            maxz = 95.0 + round(abs(djoint), 2)
            elementtodel = set()
            nodetodel = set()
            for elementkey in modelo.ElementDict.keys():
                if modelo.ElementDict[elementkey].Aux:
                    for node in modelo.ElementDict[elementkey].Nodes:
                        if node.Coords[2] < (minz) or node.Coords[2] > (maxz):
                            #nodetodel.add(node.ID)
                            elementtodel.add(elementkey)


            for elementkey in elementtodel:
                del modelo.ElementDict[elementkey]

            for nodekey in nodetodel:
                del modelo.NodeDict[nodekey]

            # Calculo de los nodos que estarán restringidos
            node_spckey = [nodo for nodo in modelo.NodeDict.keys() if modelo.NodeDict[nodo].Coords[2] == (minz)]
            node_spc = [modelo.NodeDict[nodo] for nodo in node_spckey]

            # Calculo de los nodos en los que se aplicará el desplazamiento
            node_dispkey = [nodo for nodo in modelo.NodeDict.keys() if modelo.NodeDict[nodo].Coords[2] == (maxz)]
            node_disp = [modelo.NodeDict[nodo] for nodo in node_dispkey]

            # Definicion del desplazamiento forzado
            enforce_displ = mac.set_load(id=1, type="SPC", nodes=node_disp, components=[3], displacement=enf_displ, load=True)

            # Dedfinicion de la restricción
            constr_displ = mac.set_constraint(id=2, nodes=node_disp, components=[3], displacement=enf_displ)
            constr_bot = mac.set_constraint(id=2, nodes=node_spc, components=[1,2,3], displacement=0)

            # Creación del subcaso de análisis estático lineal
            subcase_ln = mac.set_subcase(id=1, label="linear", loads=[enforce_displ],
                                         constraints=[constr_displ, constr_bot], output=["SPCFORCE"])
            # Creación del subcaso de pando lienal
            eigr1 = mac.set_eigr(id=3, type="EIGRL", numroots=10)

            subcase_buckl = mac.set_subcase(id=2, label="buckling", loads=[],
                                            constraints=[constr_displ, constr_bot],
                                            eigr=eigr1, stat_sub=subcase_ln)

            # Creación del subcaso de análisis no lineal
            nlparmld = mac.set_nlparmld(id=1, dt=0.05)
            nlout = mac.set_nlout(id=2, nint=20)
            subcase_nonln = mac.set_subcase(id=3, label="nonlinear", loads=[enforce_displ],
                                            constraints=[constr_displ, constr_bot],
                                            nlparmld=nlparmld, nlout=nlout, output=["SPCFORCE"])

            # Creación del análisis general
            analysis = mac.set_analysis(model=modelo, subcases=[subcase_ln, subcase_buckl, subcase_nonln])

            # Escritura en un archivo .fem el análisis listo para correr por optistruct
            analysis.write_fem(r"C:\Users\manum\Desktop\TFM\cubes2\\" + f"cube_{mat[count]}_v1={v1}_v2={v2}.fem" )

            # Borrado de la memoria. El uso de variables globales obliga a borrar la memoria.
            del analysis
            del modelo

    # Contador auxiliar
    count += 1
