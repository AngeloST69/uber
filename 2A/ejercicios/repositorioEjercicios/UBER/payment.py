from accountUser import User
from accountDriver import Driver

class Payment:
    id = int
    amont = int
    user = User()
    driver = Driver("", "", "", "", "")
    type = str
    def __init__(self, id, amount, user, driver, type):
        self.id = id
        self.amount = amount
        self.user = user 
        self.driver = driver