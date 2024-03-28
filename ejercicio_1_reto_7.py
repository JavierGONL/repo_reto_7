#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado

def cuadrados(lista : int) -> int:
    return lista ** 2

if __name__ == "__main__":
    lista : int = 1
    while lista <= 100:
        print("cuadrado del:",lista,cuadrados(lista))
        lista += 1
    print("Fin del while loop")