# ============================================================
#                   Tema 2: Herencia
# ============================================================

# Clase base
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f'Hola, soy {self.nombre} de {self.nacionalidad}!')


# Clase hija que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # Se usa super() para inicializar los atributos de la clase base
        super().__init__(nombre, edad, nacionalidad)
        # Nuevos atributos propios de Empleado
        self.trabajo = trabajo
        self.salario = salario

    # Sobrescritura de método saludar
    def saludar(self):
        print('Adios!!!')


# Otra clase hija de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


# Ejemplo de uso
empleado1 = Empleado("Ana", 28, "Mexicana", "Ingeniera", 1200)
estudiante1 = Estudiante("Luis", 21, "Colombiano", [4.5, 4.0, 5.0], "Universidad Nacional")

empleado1.saludar()   # Llamada al método sobrescrito -> "Adios!!!"
estudiante1.saludar() # Usa el método heredado de Persona
print(estudiante1.universidad)  # Universidad Nacional


