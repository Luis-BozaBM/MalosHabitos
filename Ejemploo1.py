def multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto


if __name__ == "__main__":
    multiplicando = float(input("Multplicando: "))
    multiplicador = float(input("Multplicador: "))
    resultado = multiplicacion(multiplicando, multiplicador)

    print(f"Resultado: {resultado} ")
