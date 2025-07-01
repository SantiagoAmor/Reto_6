# Vamos a empezar con la función
def operaciones(x, y, o):
    #! Aqui creo un match para separar cada operación 
    match o:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y
        case _:
            return "Operación Invalida"

# Bienvenida al programa e instrucciones
print("Hola, como estas?\nA continuación vas a introducir dos números y el"
      " operador que desees\n")

#* Aqui vamos a manejar las excepciones, tenemos el ZeroDivisionError para 
#* evitar la división por cero, ValueError para manejar entradas no numéricas
#* y TypeError para asegurar que los valores son números.
try:
    #! Definimos variables y pedimos sus valores
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))
    o = str(input("Ingrese el operador deseado: "))
    # Creamos la variable que contiene los resultados
    resultado = operaciones(x, y, o)
except ZeroDivisionError:
    resultado = "Error: No se puede dividir por cero."
except ValueError:
    resultado = "Error: Debes ingresar números enteros."
except TypeError:
    resultado = "Error: Los valores deben ser números."

# Mostramos resultado 
print("Resultado: ", resultado)