class Car:
    
    color = ""
    speed = 0 
    
    count = 0 #클래스 변수 
    
    def __init__(self):
        self.speed = 0 
        Car.count += 1 #Car.으로 클래스 변수 접근
        
    
    
myCar1 = Car()
myCar1.speed = 30 
print(f"자동차1의 현재 속도는 {myCar1.speed}, 생산된 자동차는 총 {Car.count}")

myCar2 = Car()
myCar2.speed = 60 
print(f"자동차2의 현재 속도는 {myCar2.speed}, 생산된 자동차는 총 {myCar2.count}")