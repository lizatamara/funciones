def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    

def productoria(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if 'fact' in clave:
            print(f'El factorial de {valor} es {factorial(valor)}')
        elif 'prod' in clave:
            print(f'La productoria de {valor} es {productoria(valor)}')

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

