def calcular(a, b, c):
    res = a * b + c
    return res

def principal():
    a = float(input("Ingrese el primer valor (a): "))
    b = float(input("Ingrese el segundo valor (b): "))
    c = float(input("Ingrese el tercer valor (c): "))
    resultado = calcular(a, b, c)
    print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    principal()

