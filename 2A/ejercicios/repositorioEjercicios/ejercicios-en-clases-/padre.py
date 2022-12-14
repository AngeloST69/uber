class Persona:
    nombre      = str
    apellido    = str
    edad        = str
    
    def __init__(self,nombre,apellido,edad) :
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def conversar(self, otra_persona):
        return f'Hola {otra_persona.nombre}me llamo {self.nombre}, estudio {self.apellido} '



class Hijo (Persona):
    ciudad = str
    
    def __init__(self, nombre, apellido, edad, ciudad):
        Persona.__init__(self,nombre,apellido,edad)
        self.ciduad = ciudad


padre=Persona('victor','grados',21)

print(vars(padre))

hijo = Hijo('victor','grados',21,'quito')
print(vars(hijo))

print(padre.conversar(hijo))

print(hijo.conversar(padre))


#agregar metodos a la herencia 

class Persona2:
    nombre      = str
    apellido    = str
    edad        = int

    
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.nombre = apellido
        
    def __init__(self,nombre,apellido,edad) :
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def conversar(self, otra_persona):
        return f'Hola {otra_persona.nombre}me llamo {self.nombre}, estudio {self.edad} '

class Hijo2(Persona2):
    estudios= str
    lugarEstudios= str
    
    def __init__(self, nombre, apellido,edad,materia,estudios,lugarEstudios):
        super().__init__(nombre, apellido,edad)
        self.materia =materia
        self.lugarEstudios = lugarEstudios
        self.estudios= estudios    

    def informar(self,otra_persona):
        return f'buenas tardes,{otra_persona.nombre} acabo de estudiar{self.materia}, llege hasta{self.estudios},mi curso es {self.lugarEstudios}'
    


padre2=  Persona2('juan','flores',25)
hijo2=Hijo2 ('juan','flores',25,'flores','flores','flores')



print(hijo2.informar(padre2))

class Padre:
    nombre = str
    apellido= str
    edad=str
    ciudad=str
    
    
    def __init__(self,nombre,apellido,edad,ciudad):
        self.nombre= nombre
        self.edad=edad
        self.ciduad=ciudad
        self.apellido=apellido
    
    def bienvenido(self,hijo):
        return f'buenas noches {hijo.nombre} bienvenido a la casa,la cena esta en el hornoyo me encuentro de viaje {self.ciduad} att - {self.nombre}{self.apellido}'
    




