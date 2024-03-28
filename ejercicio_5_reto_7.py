if __name__ == "__main__":
    numeroN = int(input("Ingrese un numero entero positivo: "))
    factorial = 1

    while numeroN > 0:
        factorial *= numeroN
        numeroN -= 1
    print("El resultado del factorial es: ", factorial)