class car(object):
    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.company=company
        self.speedlimit=speedlimit
        self.model=model
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating")
    def changeGear(self,gearType):
        print("Gear Changed")
ord=car("Super X100", "red", "WaterDogs","100")
print(ord.color)
