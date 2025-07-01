# Creamos la función
def primos(lista_primos):
    #!Creamos una lista vacia para guardar los primos
    num_primos = []
    #! Creamos un for para recorrer la lista de numeros
    for i in lista_primos:
        #! Con un if verificamos si el numero es menor a 2, pues estos no son
        #! primos
        if i < 2:
            continue
        else:
            #! Creamos una variable para verificar si el numero es primo o no
            es_primo = True
            #! Creamos un for que recorre los numeros desde 2 hasta la raiz
            #! cuadrada del numero
            for j in range(2, int(i**0.5) + 1):
                #! Si el numero es divisible por alguno de estos, no es primo
                if i % j == 0:
                    es_primo = False
                    break
            #! Si el numero es primo, lo agregamos a la lista de primos
            if es_primo:
                num_primos.append(i)
    return num_primos

# Creamos la funcion para introducir los numeros
def introducir_numeros(num):
    #! Creamos una lista para guardar los numeros
    lista_numeros_ingresa = []
    #! Creamos un for para recorrer la cantidad de numeros que el usuario
    #! desea introducir
    for i in range(num):
        i = int(input())
        lista_numeros_ingresa.append(i)
    return lista_numeros_ingresa

# Bienvenida al programa e instrucciones
print("Hola, como estas?\nA continuación vas a introducir una lista de números"
      " y veremos cuales son primos\n")

#* Aqui manejaremos la excepción ValueError para asegurarnos de que el usuario
#* ingresa números enteros.
try:
    #! Creamos la variable y pedimos sus valores
    numeros = int(input("Cuantos numeros desea introducir: "))
    print("Ingrese los numeros por favor: ")

    # Creamos una variable que contenga la lista de numeros
    lista_numeros = introducir_numeros(numeros)
    # Creamos una variable que contenga el resultado de la funcion
    lista_final = primos(lista_numeros)

    # Mostramos el resultado
    print("Los primos son: ", lista_final)
except ValueError:
    print("Error: Debes ingresar números enteros.")