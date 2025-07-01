# Creamos una primer función para verificar si dos palabras tienen los mismos caracteres
def tienen_mismos_caracteres(palabra1, palabra2):
    #! Verificamos si las palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False
    #! Verificamos si hay la misma cantidad de caracteres tanto en la primera como en la segunda palabra
    for char in palabra1:
        if palabra1.count(char) != palabra2.count(char):
            return False
    #! Hacemos lo mismo pero con la segunda palabra
    for char in palabra2:
        if palabra1.count(char) != palabra2.count(char):
            return False
    return True

# Creamos una segunda función donde introducimos la lista de palabras que 
# queremos comparar y llamamos a la primera función para verificar si tienen
# los mismos caracteres
def mismos_caracteres(lista):
    #! Creamos una lista vacia para guardar los resultados
    resultado = []
    #! Creamos un for para recorrer la lista de palabras
    for i in range(len(lista)):
        #! Creamos un for anidado para comparar una palabra con la que le sigue
        for j in range(i + 1, len(lista)):
            #! Creamos un if en el que llamamos a la funcion para que verifique
            #! si dos palabras consecutivas tienen los mismos caracteres
            if tienen_mismos_caracteres(lista[i], lista[j]):
                #! Si es asi, las agregamos a la lista de resultados, pero solo
                #! si no se encuentran ya en la lista
                if lista[i] not in resultado:
                    resultado.append(lista[i])
                if lista[j] not in resultado:
                    resultado.append(lista[j])
    return resultado

# Bienvenida al programa e instrucciones
print("Hola, como estas?\nA continuación verás una lista de palabras, ")
print("de la cual se creará otra pero solo con palabras que tengan los mismos caracteres\n")

# Creamos la lista de palabras y la mostramos
lista_palabras = ["amor", "roma", "perro", "clavel", "reop",
                   "sopa", "cosas", "arroz", "mora", "paso"]
print("Lista de palabras: ", lista_palabras)

#* Aqui manejaremos la excepción TypeError para asegurarnos de que el usuario
#* ingresa una lista de palabras (strings).
try:  
    # Mostramos el resultado final
    print("Lista de palabras con los mismos caracteres: ", mismos_caracteres(lista_palabras))
except TypeError:
    print("Error: Debes ingresar una lista de palabras (strings).")