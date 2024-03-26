import math

PI = math.pi

def calcular_area_superficial(radio:float,h:float)->float:
    l = (radio**2+h**2)**1/2
    return 4*PI*radio**2 + PI*radio*(radio+l)

def calcular_volumen_esfera_cono(radio:float,h:float)->float:
    return (4/3) * PI * radio ** 3 + PI*radio*h/3

if __name__ == "__main__":
        radio = float(input("Ingresa el radio de la esfera: "))
        h = float(input("Ingresa la altura del cono: "))
        print("el volumen de la esfera y el comoes: ", calcular_volumen_esfera_cono(radio,h))
        print("el area superficial es: ", calcular_area_superficial(radio,h))