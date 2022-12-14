from car import Car

class uberX(Car):
    asientos = int
    def __init__(self, placa, modelo, color, año, matricula, asientos):
        super().__init__(placa, modelo, color, año, matricula, asientos)
        self.asientos   = asientos