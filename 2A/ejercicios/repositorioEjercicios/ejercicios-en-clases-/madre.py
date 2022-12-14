class Madre:
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
    

