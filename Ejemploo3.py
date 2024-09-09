def f(a, b):
    result = a * b
    return result


def g(b, h):
    r = 0.5 * b * h
    return r


def main():

    x = float(input("Ingrese el primer valor (x) para el área del rectángulo: "))
    y = float(input("Ingrese el segundo valor (y) para el área del rectángulo: "))
    rect_area = f(x, y)
    print(f"Área del rectángulo: {rect_area}")

    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    tri_area = g(base, altura)
    print(f"Área del triángulo: {tri_area}")

if __name__ == "__main__":
    main()

