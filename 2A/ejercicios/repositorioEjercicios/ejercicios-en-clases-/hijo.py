from padre import Persona
from padre import Persona2
from madre import Madre
from padre import Padre

#ruta
#solo se puede si esta en la misma carpeta


class hijo3(Persona):
    vivienda=str
    
    def __init__(self, nombre, apellido, edad,vivienda):
        super().__init__(nombre, apellido, edad)
        self.vivienda=vivienda

hijo3=hijo3 ('diego','yanez',28,'centro de estudios')
padre3= Persona('diego','yanez',28)

print(vars(hijo3))
print(vars(padre3))
print(hijo3.conversar(padre3))


class Hijo4(Persona2):
    edad=int
    semestre=str
    def __init__(self, nombre, apellido, edad,semestre):
        super().__init__(nombre, apellido, edad)
        self.edad=edad
        self.semestre=semestre   
        
        
    def felicitar(self,padre):
        return f'felicitaciones{self.nombre},acabas de terminar tu {self.semestre} semestre a tus {self.edad} años de edad. att{padre.nombre}{padre.apellido} ' 
    
    
    
padre4= Persona2('diego','yanez')
hijo4= Hijo4('diego','yanez',28,'quinto')


print(vars(padre4))
print(vars(hijo4))
print(hijo4.felicitar(padre4))

class HijoFinal(Madre):
    nombre=str
    apellidoPaterno=str
    apellidoMaterno=str
    
    madre =Madre('','','','')
    
    def __init__(self, nombre, apellidoPaterno,apellidoMaterno, edad,madre):
        super().__init__(nombre, edad )
        self.apellidoPaterno=apellidoPaterno
        self.apellidoMaterno=apellidoMaterno
        
        self.madre=madre
        
        
        
padreFinal=Padre('german','yanez',55,'quito')
madreFinal= Madre('german','yanez',55,'quito')
#hijoFinal= HijoFinal('diego','yanez','flores',55,Madre('german','yanez',55,'quito'))
#hijoFinal= HijoFinal('diego','yanez','flores',29,Madre{'veronica,flores',55,'quito'})
print(vars(padreFinal))
print(vars(madreFinal))
#print(vars(hijoFinal))