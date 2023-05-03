
try:
    import sys
    sys.path.insert(0, r'C:\MAC\v.0.0')
    import MetamaterialAnalysisCode as MAC
except ImportError:
    print('Some modules where not found')

clase_1 = MAC.calse_prueba()
clase_1.set_a(10)
clase_1.set_b(5)
print(MAC.calse_prueba.division(clase_1))

