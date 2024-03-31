if __name__ == "__main__":
    print("este programa adivinada el numero que estas pensando")
    print("Piensa en un numero entero entre 1 y 100")
    print("El programa intentara adivinar el numero que estas pensando")
    print("Si el numero que el programa te da es mayor que el tuyo escribe 'M'")
    print("Si el numero que el programa te da es menor que el tuyo escribe 'm'")
    print("Si el numero que el programa te da es el correcto escribe 'OK'")
    print("en un punto te preguntara mas informacion que se respondera de manera diferente")
    
    while True:
        minimo = 1
        maximo = 100
        while True:
            numero = (minimo + maximo) // 2
            print("Estas pensando en el numero", numero, "?")
            respuesta = input("Escribe 'M', 'm' o 'OK': ")
            if respuesta == "OK":
                print("El programa ha adivinado el numero que estabas pensando")
                break
            elif respuesta == "m":
                maximo = numero - 1
            elif respuesta == "M":
                minimo = numero + 1
            elif respuesta == "salir":
                break
            else:
                print("ingrese solo las letras establecidas")
        