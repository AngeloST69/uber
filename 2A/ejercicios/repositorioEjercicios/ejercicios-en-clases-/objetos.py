class miClase:
    x = 5


p1 = miClase()
print(p1.x)


class persona:
    nombre = str
    edad = int

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Su nombre es {self.nombre}. y edad es: {self.edad}."


p2 = persona("Diego", 29)

print(p2)


class Persona2:
    nombre = str
    edad = int
    cedula = int


def __init__(self, nombre, edad, cedula):
    self.nombre = nombre
    self.edad = edad
    self.cedula = cedula


def miFuncion(self):
    print("Hola mi nimbre es " + {self.nombre} +
          "Con mi numero de cedula" + {self.cedula})


p3 = Persona2("alexander", 32, 172108007)
p3.miFuncion()

p3.nombre = "Carlos"
p3.cedula = "23231231242"


class persona3:
    nombre = str
    edad = int
    estatura = int

    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura

    def __str__(self):
        return f"Su nombre es{self.nombre}. y edad es: {self.edad} .y su estatura {self.estatura}"


p4 = persona3("Diego", 29, 99)

print(p4)
