class Car:
    
    speed = 0
    def upSpeed(self, value): 
        
        self.speed += value 
        
        print(f"현재속도(슈퍼클래스) : {self.speed}")
        
class Sedan(Car):
    def upSpeed(self, value):
        
        self.speed += value 

        if self.speed > 150:
            
            self.speed = 150 
            
        print(f"현재속도(서브클래스) : {self.speed}")
        
class Truck(Car):
    pass 

sedan1, truck1 = None, None 

truck1 = Truck()
sedan1 = Sedan()

print(f"트럭 --> ", end="")
truck1.upSpeed(200)

print(f"승용차 -->", end="")
sedan1.upSpeed(200)