#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. 
#Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. 
#Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

if __name__ == "__main__":
    pais_A_poblacion : float = 22000000
    pais_B_poblacion : float = 18900000
    tasa_crecimiento_pais_A : float = 0.02
    tasa_crecimiento_pais_B : float = 0.03
    tiempo : int = 0
    while pais_B_poblacion < pais_A_poblacion:
        pais_A_poblacion = pais_A_poblacion * (1 + tasa_crecimiento_pais_A) ** tiempo
        pais_B_poblacion = pais_B_poblacion * (1 + tasa_crecimiento_pais_B) ** tiempo
        tiempo += 1
    print("desdes el 2022 La población de B supero a la poblacion de A en", tiempo, "años")
    print("Población de A:", pais_A_poblacion)
    print("Población de B:", pais_B_poblacion)
