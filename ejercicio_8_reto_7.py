def es_primo (numero):
  conteo=2
  divisores=1
  while conteo<=numero and divisores <=2:
    comprobacionSiEsDivisor = numero % c
    if comprobacionSiEsDivisor == 0:
      divisores=divisores+1
    c=c+1
  if divisores == 3:
    return False
  else: 
    return True
  
if __name__ == "__main__":
    numero=0
while numero<=100:
  if es_primo(numero):
    print(numero)
  n=n+1
print("Fin del ejercicio 8 reto 7 ")