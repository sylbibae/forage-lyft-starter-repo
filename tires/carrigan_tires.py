from tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self, tire_wear):
        for wear in tire_wear:
            if wear > 0.9:
                return True
        