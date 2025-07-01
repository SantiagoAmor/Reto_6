# Creamos la funcion
def mayor_suma_consecutivos(lista):
    #! Con un if verificamos si la lista tiene menos de 2 elementos
    #! Si es asi, no podemos calcular la suma de dos consecutivos
    if len(lista) < 2:
        return None
    #! Creamos una variable para guardar la suma mayor
    mayor_suma = lista[0] + lista[1]
    #! Creamos un for para recorrer la lista
    for i in range(1, len(lista) - 1):
        #! Creamos una variable para guardar la suma de los dos consecutivos
        suma_actual = lista[i] + lista[i + 1]
        #! Comparamos la suma actual con la mayor suma
        if suma_actual > mayor_suma:
            #! Si la suma actual es mayor, la guardamos en la variable
            #! mayor_suma
            mayor_suma = suma_actual
    return mayor_suma

# Creamos la funcion para introducir los numeros
def introducir_numeros(num):
    #! Creamos una lista para guardar los numeros
    lista_numeros_ingresa = []
    #! Creamos un for para recorrer la cantidad de numeros que el usuario desea
    #! introducir
    for i in range(num):
        i = int(input())
        lista_numeros_ingresa.append(i)
    return lista_numeros_ingresa

# Bienvenida al programa e instrucciones
print("Hola, como estas?\nA continuación vas a introducir una lista de números"
      " y veremos cual es la mayor suma de consecutivos\n")

#* Aqui manejaremos la excepción ValueError para asegurarnos de que el usuario
#* ingresa números enteros.
try:
    #! Creamos la variable y pedimos sus valores
    numeros = int(input("Cuantos numeros desea introducir: "))
    print("Ingrese los numeros por favor: ")

    # Creamos una variable que contenga la lista de numeros
    lista_numeros = introducir_numeros(numeros)
    # Creamos una variable que contenga el resultado de la funcion
    mayor_suma_final = mayor_suma_consecutivos(lista_numeros)

    # Mostramos el resultado
    print("La mayor suma de números consecutivos es: ", mayor_suma_final)
except ValueError:
    print("Error: Debes ingresar números enteros.")