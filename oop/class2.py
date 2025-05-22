class Car : 
    
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        
        self.color = value1
        self.speed = value2
        
    def upSpeed(self, value):
        
        #self 중요, self를 통해서 매서드 작동동
        
        self.speed += value
        
        # self 쓰면은 클래스의 필드(속성)을 건드린다는뜻뜻
        
        if self.speed >= 150:
            
            self.speed = 150
        
    def downSpeed(self, value):

        self.speed -= value
        
myCar1 = Car("빨강", 30)
myCar2 = Car("파랑", 60)

print(f"자동차1의 색상은 {myCar1.color}이며, 현재 속도는 {myCar1.speed}입니다")

print(f"자동차2의 색상은 {myCar2.color}이며, 현재 속도는 {myCar2.speed}입니다")