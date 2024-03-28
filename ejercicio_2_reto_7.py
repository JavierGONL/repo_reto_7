#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000

if __name__ == "__main__":
    pares : int = 2
    impares : int = 1

    while pares <= 1000:
        print("pares:",pares)
        pares += 2
    print("Fin del while loop pares")

    while impares <= 1000 and impares % 2 != 0:
        print("impares:",impares)
        impares += 2
    print("Fin del while loop impares")