#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

if __name__ == "__main__":    
    numeroN = int(input("Ingrese un número: "))
    if numeroN % 2 == 0:
        while numeroN >= 2 and numeroN % 2 == 0:
            print(numeroN)
            numeroN -= 2
    else:
        numeroN -= 1
        while numeroN >= 2 and numeroN % 2 != 0:
            print(numeroN)
            numeroN -= 2

