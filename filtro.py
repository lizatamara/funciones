import sys

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtrar(umbral, mayor_o_menor):
    if mayor_o_menor == "mayor":
        filtro = {k:v for k,v in precios.items() if v > umbral}
        print(f"Los productos mayores al umbral son: " + ", ".join(filtro))
    elif mayor_o_menor == "menor":
        filtro = {k:v for k,v in precios.items() if v < umbral}
        print(f"Los productos menores al umbral son: " + ", ".join(filtro))
    else:
        print(f"Lo sentimos, no es una operación válida")

umbral = int(sys.argv[1])

if len(sys.argv) == 3:
    mayor_o_menor = sys.argv[2]
else:
    mayor_o_menor = "mayor"


filtrar(umbral, mayor_o_menor)
