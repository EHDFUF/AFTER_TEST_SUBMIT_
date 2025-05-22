class Car : 
    
    name = ""
    speed = 0
    
    def __init__(self, name, speed):
        
        self.name = name 
        self.speed = speed
        
    def getName(self):
        return self.name 
    
    def getSpeed(self):
        return self.speed 

car1 = Car("아우디", 0)
car2 = Car("밴츠츠", 30)

print(f"{car1.getName()}의 현재 속도는 {car1.getSpeed()}")

print(f"{car2.getName()}의 현재 속도는 {car2.getSpeed()}")