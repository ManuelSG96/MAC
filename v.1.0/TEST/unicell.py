import MetamaterialAnalysisCode as mac

# Unidades en milimetros

enf_displ = -15  # Desplazamiento forzado

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
v1 = -0.8
v2 = 0.25

# Dimensiones del modelo:
dim = (20, 20, 20)

# Calculo de parametros geometricos a partir de v1 y v2
djoint = v1*hcapas/2
heightstar = v2*djoint

# Definiciónde la estructura de la celda
cellstructure = mac.set_structure(type="Auxetic", djoint=djoint, dstar=dstar, heightstar=heightstar, hcapas=hcapas,
                                  hprisma=hprisma, stepx=stepx, stepy=stepy, nelem=1)

# Definicion del modelo
modelo = mac.set_model(modeldimensions=dim, cellstructure=cellstructure,
                       cellmaterial=[vigas[0].Material[0]], cellproperty=[vigas[0]])

modelo.write_fem(r"C:\Users\manum\Desktop\TFM\celdaunidad1.fem")
