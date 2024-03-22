import sys

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtrar(umbral, mayor_o_menor = "mayor"):
    if mayor_o_menor == "mayor":
        filtro = {k:v for k,v in precios.items() if v > umbral}
        print(f"Los productos mayores al umbral son: " + ", ".join(filtro))
    elif mayor_o_menor == "menor":
        filtro = {k:v for k,v in precios.items() if v < umbral}
        print(f"Los productos menores al umbral son: " + ", ".join(filtro))
    else:
        print(f"Lo sentimos, no es una operación válida")

filtrar(int(sys.argv[1]), sys.argv[2])

# si no pongo ningún argumento en el 2do parámetro me da error, pero no supe cómo corregirlo
