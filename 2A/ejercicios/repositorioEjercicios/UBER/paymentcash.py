from payment import Payment

class paymentCash(Payment):
    def __init__(self, id, amount, user, driver, type):
        super().__init__(id, amount, user, driver, type)
    
    