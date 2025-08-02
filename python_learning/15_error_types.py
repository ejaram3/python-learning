# Tema : Error types

""" 
En python se refiere a exepciones que se lanzan cuando falla la ejecución del código. Entenderlos permite manejar errores de forma precisa con bloques try-except
"""

# Errores de sintaxis
# if True print("Hola") # SyntaxError

# def f():
# print("Error") # IndentationError

# Errores de tiempo de ejecución
# 6 + "4" # TypeError

# int("abc") # ValueError

# print(a) # NameError

# def f():
#     print(x)
#     x = 4
# print(f()) # UnboundLocalError

# l = [1, 3]
# l[3] # IndexError

# d = {"a" : 11}
# print(d["b"]) # KeyError

# 3 / 0 # ZeroDivisionError

# import math
# math.exp(1000) # OverflowError

# open("My_file.txt") # FileNotFoundError

# open("/protegido.txt", "w") # PermissionError, IOError

# Manejo de errores
try: 
    # print(10 / 0)
    print(1 + "2")
except ZeroDivisionError as err:
    print("No Puedes dividir por Cero:", err)
except Exception as e:
    print("Otro Error:", e)

print("Sigue el codigo...")



def print_exception_hierarchy(exception_class, indent=0):
    """
    Imprime en consola la jerarquía de clases de excepción derivadas de una clase base dada.

    Parámetros:
        exception_class (type): Clase base desde la cual comenzar la exploración. 
                                Usualmente se pasa 'Exception' o 'BaseException'.
        indent (int): Nivel de sangría para representar jerarquía visualmente. Se incrementa recursivamente.

    Comportamiento:
        - Usa __subclasses__() para obtener las subclases directas de exception_class.
        - Imprime el nombre de cada subclase con sangría proporcional a su nivel de herencia.
        - Recorre recursivamente toda la jerarquía de excepciones derivadas.

    Ejemplo de uso:
        print_exception_hierarchy(Exception)
    """
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)


print_exception_hierarchy(Exception)