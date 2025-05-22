class Car :
    #자동차필드(자동차클래스속성)
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        
        #self 중요, self를 통해서 매서드 작동동
        
        self.speed += value
        
        # self 쓰면은 클래스의 필드(속성)을 건드린다는뜻뜻
        
        if self.speed >= 150:
            
            self.speed = 150
        
    def downSpeed(self, value):

        self.speed -= value 
        
    def printNessage():
        print("시험출력")
    
myCar1 = Car()
myCar2 = Car()
myCar3 = Car()
 
myCar1.color = "빨강"
myCar1.speed = 0

myCar2.color = "파랑"
myCar2.speed = 0

myCar3.color = "노랑랑"
myCar3.speed = 0

myCar1.upSpeed(200)
myCar2.downSpeed(20)

print(f"자동차1의 색상은 {myCar1.color}이며, 현재 속도는 {myCar1.speed}입니다")

print(f"자동차2의 색상은 {myCar2.color}이며, 현재 속도는 {myCar2.speed}입니다")

print(f"자동차3의 색상은 {myCar3.color}이며, 현재 속도는 {myCar3.speed}입니다")