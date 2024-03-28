def divisores (numeroN,divisor)->float:
    if numeroN % divisor == 0:
        return True 
    else:
        return False
    
if __name__ == "__main__":
    numeroN = int(input("Ingrese un numero entero positivo(numero entre 2 y 50): "))
    if numeroN < 2 or numeroN > 50:
        print("El numero ingresado no es valido")
    else:
        divisor = 2
        while divisor <= numeroN and numeroN < 50:
            if divisores(numeroN,divisor):
                print(divisor)
            divisor += 1 
        print("Fin del ejercicio 7 reto 8 ")