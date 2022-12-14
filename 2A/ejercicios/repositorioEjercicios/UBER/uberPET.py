from car import Car

class uberPET(Car):
    trasportePet  = bool
    
    def __init__(self, placa, modelo, color, año, matricula, trasnportePet, driver):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.trasportePet = trasnportePet
    