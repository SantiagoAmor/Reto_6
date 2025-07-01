# Creamos la función
def palindromo(palabra):
    #! Creamos una variable para introducir la palabra invertida
    palabra_2 = ""
    #! Con un for recorremos la palabra y la introducimos alreves en la nueva
    #! variable
    for i in range(len(palabra)-1, -1, -1):
        palabra_2 += palabra[i]
    #! Comparamos las palabras y con el if damos el resultado
    if palabra_2 == palabra:
        return True
    else:
        return False
    
# Damos la bienvenida e instrucciones
print("Hola, como estas?\nA continuación vas a introducir dos una palabra y "
      "veremos si es políndromo o no\n")

#! Creamos variable y pedimos su valor
palabra_palindromo = str(input("Ingrese una palabra (toda la palabra en minus"
"cula): "))

# Creamos una variable que contenga el resultado de la funcion
resultado = palindromo(palabra_palindromo)

# Mostramos el resultado
print("La palabra \"", palabra_palindromo, "\" es palíndromo?\n", resultado)

#* Aqui no hay manejo de excepciones porque la funcion toma texto al ser
#* ingresado por un input, por ende no hay error, sencillamente se devuelve
#* False si no es palindromo y True si lo es.