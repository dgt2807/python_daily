#class
#function으로 만들면
result =0
result2 =0
def add(num):
    global result
    result +=num
    return result
def add2(num):
    global result2
    result2 += num
    return result2

print(add(3))
print(add(4))
print(add2(3))
print(add2(4))
#class를 사용하면(설계도)
#구조
         #class Name :      #클래스명 대문자로 시작해야 한다(약속)
         #내용
#설계도_틀
class Calculator:
    def __init__(self):     #함수 이지만 정확히는 메서드
        self.result =0
        
    def add(self, num):
        self.result +=num
        return self.result
    
    def sub(self,num):      #기능추가도 가능 설계도니까
        self.result -=num
        return self.result
    
cal1 =Calculator()          #두개의 인스턴스_객체_오브젝트를 만들어줌
cal2 =Calculator()          #독자적인 서로 영향을 미치지 않는 고유한 대상이 됨

print(cal1.add(5))
print(cal2.add(4))
#
class Cookie:
    pass
a=Cookie()                  #a는 객체 이고 a 객체는 Cookie의 인스턴스 이다(관계)
b=Cookie()                  #p187
#생성자                     필드값을 초기화하는 함수,객체에 초기값 설정해야 할때 
        #__init__()         #__ 파이썬에서 예약한 것
        #초기화할 코드 들어감
#
class FourCal():
    def __init__(self,first,second):#생성자 p.199  얘가 있으면 아래 초기화 함수 없어도.
        self.first=first
        self.second=second    
                 #a.setdata(4,2)    #초기값 설정 메소드
    #def setdata(self,first,second): #self 는 객체 자신을 의미 (관례적), p192
    #    self.first=first            #a.first가 a.setdata(4)가  
    #    self.second =second         #a.second가 a.setdata(2)됨

    def add(self):
        result = self.first+self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def div(self):
        result = self.first/self.second
        return result
    def sub(self):
        result = self.first-self.second
        return result
        
    
a=FourCal()                 #객체를 지정하고
a.setdata(4,2)              #메서드 사용 , 객체의변수 생성 -> 생성자 있으면 불필요
id(a.first)
id(a.second)
a.add()                 #주소확인 id()
a.mul()
a.sub()
a.div()

b=FourCal()
b.setdata(7,2)
id(b)               #주소 가고 있
id(b.first)         #숫자 같으면 주소같음
id(b.second)
# 생성자를 지정했을 때 (set부분 닫음) [line50]
a=FourCal(4,2)                 
a.add()                
a.mul()
a.sub()
a.div()
#상속 inheritance
class MoreFourCal(FourCal):     #상속 받는 클래스 생성시 '클래스명(부모클래스):'
    #pass
    def pow(self):              #메소드 추가
        result=self.first** self.second
        return result
    #메서드 오버라이딩 (부모 클래스 고유_클래스의 메서드와 이름 같음_기능을 변형)    
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

a=MoreFourCal(10,2)
a.add()
a.pow()
b=MoreFourCal(10,0)
b.div()
#class varible  클래스 내에 선언한 변수
class Family:
    lastname ='김'
print(Family.lastname)
    #클래스로 만든 객체의 변수 값도 모두 변경된다.
Family.lastname="박"
a=Family()
b=Family()
print(a.lastname)
#
class Car:
    #def __init__(self,color,speed):     안됨 다시해볼것
    #    self.color=""
    #    self.speed=0
    color=""
    speed=0
    
    #def __init__(self):
    #    self.color= "빨강"
    #    self.speed=0
    
    #def __init__(self,value1,value2):
       # self.color= value1
       # self.speed= value2
    
    #def upSpeed(self,value):
       # self.speed+=value
       # if self.speed >150:
       #     self.speed=150
    #def downSpeed(self,value):
       # self.speed-=value
    
    name =""
    speed=0
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        
    def getName(self):
        return self.name
    def getSpeed(self):
        return self.speed
       
       
        #
myCar1=Car()
myCar1.color="빨강"
myCar1.speed=0     

myCar2=Car()
myCar2.color="파랑"
myCar2.speed=0    

myCar3=Car()
myCar3.color="노랑"
myCar3.speed=0         

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며 , 현재 속도는 %dkm입니다."%(myCar1.color,myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며 , 현재 속도는 %dkm입니다."%(myCar2.color,myCar2.speed))

myCar3.upSpeed(180)
print("자동차3의 색상은 %s이며 , 현재 속도는 %dkm입니다."%(myCar3.color,myCar3.speed))
    #[lin127]추가 __init__
myCar4=Car()
myCar5=Car()
print("자동차4의 색상은 %s이며 , 현재 속도는 %dkm입니다."%(myCar4.color,myCar4.speed))
print("자동차5의 색상은 %s이며 , 현재 속도는 %dkm입니다."%(myCar5.color,myCar5.speed))
    #[line131] __init__ (self,value1,value2)
myCar6=Car("빨강",30)
myCar7=Car("보라",60)
print("자동차6의 색상은 %s이며 , 현재 속도는 %dkm입니다."%(myCar6.color,myCar6.speed))
print("자동차7의 색상은 %s이며 , 현재 속도는 %dkm입니다."%(myCar7.color,myCar7.speed))
    #[line142] __init__ (self,name,speed)
myCar8=Car("아우디",0)
myCar9=Car("밴츠",60)
print("%s의 현재 속도는 %dkm입니다."%(myCar8.name,myCar8.speed))
print("%s의 현재 속도는 %dkm입니다."%(myCar9.name,myCar9.speed))
#######################################################################
# 모듈 불러오기
import sys                 #기본 라이브러리 포함
print(sys.path)
sys.path.append("C:\doit") #경로 추가해줌

import mod1
print(mod1.add(3,4))    #그래서 가져옴

from mod1 import add
add(3,5)
#from mod1 import add,sub
#from mod1 import*
#sub(144,22)
#
from mod1 import func1,func2,func3
func2()
mod1.func3()
#
import mod1      #import만 시켜도 실행이된다. mod1.py[line7]
#
import mod1   
############################################################################              
#package 파이썬 모듈을 관리하는 도구
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()
#import game을 수행하면 game 디렉터리 의 모듈 또는 game 디렉터리 __init__에 정의 한것만 참조하기에 전부불어야한다.
#p.219 도트연산자() ~~ 주의 깊게 읽을것
#init.py는 해당 디렉터리가 패키지으 일부임을 알려주는 역할 없다면 패키지로 인식하지 않는다.
from game.sound import*
echo.echo_test()
#relative패키지
########################################################################
#https://python.bakyeono.net/chapter-9-4.html#941-%EC%98%88%EC%99%B8%EC%9D%98-%EB%B6%84%EB%A5%98
#예외처리               p.230까지
    #오류가 발생  구문오류  EOL문자열 닫지 않음 , 예외오류 
    #예외처리를 수행
try:
    4/0
except ZeroDivisionError as e:
    print(e)
#isdigit() int()함수에서 숫자로 변환할 수 없는 문자열 변환 문제 회피
user_input_a = input("정수 입력>")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름:",number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이",3.14*number_input_a * number_input_a)
else:
    print("정수를 입력하라고")
#
try:
    f=open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.cloes()    
#
try:
    a=[1,2]
    print(a[4])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
#오류회피
try:
    f=open("없는 파일",'r')
except FileNotFoundError as e:
    print(str(e))
    pass
#오류 발생시키기  raise
class Bird:
    def fly(self):     #정의 되지 않으면  에러 발생
        raise NotImplementedError

class Eagle1(Bird):
    pass

eagle =Eagle1()
eagle.fly()


class Eagle(Bird):
    def fly(self):
        print("Very fast")

eagle =Eagle()
eagle.fly()
######################################################################
#내장함수 invalid
#절대값
abs(-3)
#모두 참인지 검사 0_false
all([1,2,3,0])
#하나라도 참인지
any([1,2,3,0])
any([0,""])    
#ascii
chr(97)
chr(48)
#딕셔너리  객체가 자체적으로 가진 변수 , 함수
dir([1,2,3])
dir({'1':'a'})
#enumerate   _많이씀
divmod(7,3)
# 현재 값을 인덱스와  같이  볼 수 있음
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
#eval
eval('1+2')
eval("'hi'+'a'")
eval('divmod(4,3)')
#fliter  _많이씀   
def positive(x):
    return x>0  
print(list(filter(positive,[1,-3,2,0,5,6])))    #positive 양수값
print(list(filter(lambda x: x>0,[1,-3,2,0,-5,6]))) # filter lamda _많이씀
#
hex(234)
#id  input 지나침
#int
int('3')
int(3.4)
int('11',2) #2진수로 표현된 11의 10진수값
#isinstance  여부 확인
class Person: pass
a =Person()
isinstance(a,Person)
True
#zip  동일한 개수로 이루어진 자료형을 묶어 주는 역할_많이씀
list(zip([1,2,3],[4,5,6]))
list(zip([1,2,3],[4,5,6],[7,8,9]))
list(zip('abc','def'))
########################################################################
#외장함수 _라이브러리
#glob_대량의 파일 한번에가져올때
# 데이터 가져오는 동안 잠깐 재운다? time.sleep
import time 
for i in range(10):
    print(i)
    time.sleep(1)
#random  random.shuffle()
import random
data =[1,2,3,4,5]
random.shuffle(data)
data
#
    
