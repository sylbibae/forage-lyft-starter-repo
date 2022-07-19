from tires import Tires 

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self, tire_wear):
        sum = 0
        for tire in tire_wear:
            sum += tire
        if sum >= 3:
            return True
        else:
            return False 