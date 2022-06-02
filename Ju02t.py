#
h,i=0,0
for i in range(1,101):
    h+=i
    print(i,h)
    if h>=1000:
        break
    
print("1~100 합이 1000이상 되는 숫자 %d"%i)
#
h,i=0,0
for i in range(1,101):
    if i%3==0:
        print(i,h,"제외")
        continue
    print(i,h)
    h+=i
print("1~100 합 3배수 제외 %d"%h)
##1  #---이거 틀림-----    
#1부터 1000까지 홀수 합계 최초 1000 넘는 숫자 구하기
h,i=0,0
for i in range(1,101):
    if i%2==0:
        continue
    h+=i
    print(i)
    if h>1000:
        break
print(h)
##2
numbers =[55,5,15,6,20,7,25,43]
for i in numbers:
    if i< 10:
        continue
    print(i)
#
aa=[]
for i in range(0,4):
    aa.append(0)
h = 0
for i in range(0,4):
    aa[i]= int(input(str(i+1)+"번째  숫자:"))
    #print(aa[3]) print문 중간 삽입(중요)
h=aa[0]+aa[1]+aa[2]+aa[3]
print(h)
#
aa=[]
bb=[]
value=0
for i in range(0,100):
    aa.append(value)
    value+=2
print(aa[0],aa[99])
 #aa.reverse 여기선 되는데
for i in range(0,100):
    #bb.append(aa.reverse())를 하려면 line56_bb.append(aa[i+1])로 대체 해야겠지
    #bb=aa.reverse() 이건 for문 밖에서 해도 안됨 _'NoneType' object is not subscriptable
    bb.append(aa[99-i])
    print(bb)
print(bb[0],bb[99])    
#  jiral hane .
m=[30,20,10]
print("%s"%m)

m.append(40)
print(m) 
print("%s"%m)
print(m.append(50))  # 결과 는 none 나오고 list m에 추가됨

print(m.pop())   #결과는 40 list m에 제거됨 
print(m)

    #sort sorted다름 https://inma.tistory.com/137
m.sort()
m.reverse()
m.insert()
m.remove()
m.extend()
m.count()

#  문제 있음. 만들어 보자 , key 안의 음식 입력하면 출력되는 코드였음
o={"A":"a","B":"b","V":"v","C":"c","D":"d","Z":"z","S":"s"}
list(o.keys())
while(True):
    a = input(str(list(o.keys()))+"Key")
    if a in o:
        print("Y")
    elif a=="End":
        break
    else:
        print("N")
#위와 같은 건데
foods={"떡볶이":"오뎅"}
while(True) :
    myfood=input(str(list(foods.keys()))+"좋아하는 음식은?")
    if myfood in foods:
        print("%s"%foods.get(myfood))
    elif myfood =="끝" :
        break
    else:
        print("없음")
#function
def a(a,b):   #parameter(매개변수)   a,b
    return a+b
x=300
a(x,70)      #argument(인자)  x,70
#    
def s(x,y):
    return x-y
s(40,30)    
#
def sum(a,b):
    result = a+b
    return result  #return 값에 주목
a= sum(3,4)
print (a)
#    
def say():
    return 'HI'
a=say()
print(a)    #return value 가 있지만 입력값(인자)이 없는 함수
#return값 없는 함수
def sum(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))
sum(3,4)
a=sum(3,4)
print(a)   #none이 뜬다
# 입력값도 return도 없음
def say():
    print('HI')
say()
#
coffee=0
coffee= int(input("어떤 커피를 드릴까요?(1 보통,2 설탕,3 블랙)"))
print()
print("#1. 뜨거운 물을 준비한다")
print("#2. 종이컵을 준비한다")
      
if coffee==1:
    print("#3. 보통커피를 탄다")
elif coffee==2:
    print("#3. 설탕커피를 탄다")
elif coffee==3:
    print("#3. 블랙커피를 탄다")
else:
   print("#3. 아무거나 탄다\n")
print("#4. 물을 붓는다")
print("#5. 스푼으로 젓는다.")
print()
print("커피 나왔다")
#
coffee=0#전역변수 선언
    #함수 선언부
def coffee_machine(button):
    print()
    print("#1. 뜨거운 물을 준비한다")
    print("#2. 종이컵을 준비한다")
          
    if coffee==1:
        print("#3. 보통커피를 탄다")
    elif coffee==2:
        print("#3. 설탕커피를 탄다")
    elif coffee==3:
        print("#3. 블랙커피를 탄다")
    else:
       print("#3. 아무거나 탄다\n")
    print("#4. 물을 붓는다")
    print("#5. 스푼으로 젓는다.")
    print()
    #메인
battery = 10
for i in range(battery):    
    get_coffee= int(input("어떤 커피를 드릴까요?(1 보통,2 설탕,3 블랙)"))
    coffee_machine(get_coffee)
    print("커피 나왔다, battery 잔량:10/ %d"%i)
#
visitor =int(input("몇명인가"))    
for i in range(visitor):
    get_coffee= int(input("어떤 커피를 드릴까요?(1 보통,2 설탕,3 블랙)"))
    coffee_machine(get_coffee)
    print("%d번째, 커피 나왔다" %i)
#
##주의깊게 볼것
coffee=0#전역변수 선언
    #함수 선언부
def coffee_machine(button):
    print()
    print("#1. 뜨거운 물을 준비한다")
    print("#2. 종이컵을 준비한다")
          
    if button==1:
        print("#3. 아메리카노를 탄다")
    elif button==2:
        print("#3. 카페라떼를 탄다")
    elif button==3:
        print("#3. 카푸치노를 탄다")
    elif button==4:
        print("#3. 에스프레소를 탄다")
    
    else:
       print("#3. 아무거나 탄다\n")
    print("#4. 물을 붓는다")
    print("#5. 스푼으로 젓는다.")
    print()
    
BP=["로제","리사","제니","지수"]
for i in BP:
    get_coffee= int(input("어떤 커피를 드릴까요?(1 아메리카노,2 카페라떼,3 카푸치노,4 에스프레소)"))
    coffee_machine(get_coffee)
    print("%s 님, 커피 나왔다"%i )
#
    #함수 선언부
def coffee_machine(button):
    print()
    print("#1. 뜨거운 물을 준비한다")
    print("#2. 종이컵을 준비한다")
          
    if gf==1:
        print("#3. 아메리카노를 탄다")
    elif gf==2:
        print("#3. 카페라떼를 탄다")
    elif gf==3:
        print("#3. 카푸치노를 탄다")
    elif gf==4:
        print("#3. 에스프레소를 탄다")
    
    else:
       print("#3. 아무거나 탄다\n")
    print("#4. 물을 붓는다")
    print("#5. 스푼으로 젓는다.")
    print()
    
BP=["로제","리사","제니","지수"]
for i in BP:
    gf= int(input("어떤 커피를 드릴까요?(1 아메리카노,2 카페라떼,3 카푸치노,4 에스프레소)"))
    coffee_machine(gf)
    print("%s 님, 커피 나왔다"%i )

#
def plus(v1,v2):
    result =0
    result = v1+v2
    return result
h=0
h=plus(100,200)
print(h)
#
def calc(v1,v2,op):
    result=0
    if op =='+':
        result=v1+v2
    elif op =='-':
        result=v1-v2
    elif op =='*':
        result=v1*v2
    elif op =='/':
        result=v1/v2
    return result
res, var1,var2,oper=0,0,0,""
oper = input("계산을 입력하세요(+,-,*,/) :")
var1 = int(input("첫 번째 수를 입력하세요 :"))
var2 = int(input("두 번째 수를 입력하세요 :"))
res= calc(var1,var2,oper)
print("계산기 : %d%s%d =%d"%(var1,oper,var2,res))
#
def func1():
    result=100
    return result
def func2():
    print("반환하는 값이 없는 함수 실행")
h=0

h=func1()
print("func1()에서 돌려준 값==>%d"%h)
func2()
#
import random
def getNumber():
    return random.randrange(1,46)
lotto=[]
num=0
print("추첨시작\n");
while True:
    num=getNumber()
    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto) >=6:  #==
        break
print("추처된 로또 번호==>",end='')
lotto.sort()
for i in  range(0,6):
    print("%d"%lotto[i],end='')
# *_ 파라미터가 개수가 다수이고 미정일떄
def sum_many(*args):
    sum=0
    for I in args:
        sum+=I
    return sum
result = sum_many(1,2,3,4,5,6)
print(result)
#
def add_mul(choice,*a):
    if choice =="add":
        result =0
        for i in a:
            result += i
    elif choice =="mul":
        result =1
        for i in a:
            result *=i
    return result
result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)
#
def sum_and_mul(a,b):
    return a+b, a*b
result =sum_and_mul(3,4)
print(result)
    #위와 같지 않고 두번쨰 return a*b는 반환되지 않는다,
def sum_and_mul(a,b):
    return a+b
    return a*b
result =sum_and_mul(3,4)
print(result)
# if_True else_False
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("001",235,True)
#지역변수
a=1 #전역변수
def vartest(a):
    print(a)
    a+=1  #지역변수 이기 떄문에 vartest 안에서만 적용되고 만다
    print(a)
vartest(a)
print(a)
#
a=1
def vartest1(a):
    print(a)
    a+=1
    print(a)    
    return a   
a = vartest1(a)
print(a)
#
a=1
def vartest2():
    global a  # 지역변수를 전역변수화
    a+=1
vartest2()
print(a)
#
def func1():
    #global a 여기서 전역변수 선언이 되면 밖에서 전역변수를 지정해줘도 무시된다
    a=10
    print("func1()에서 a값 %d" %a)

def func2():
    print("func2()에서 a값 %d" %a)
a=20 #전역변수

func1()
func2()
#input
a= input()
a
#########################################################################
print("life" "is too" "short")
print("life"+"is too"+"short")
print("life", "is too", "short")
for i in range(10):
    print(i,end='')
#r읽기 w 쓰기 a추가         
f= open("C:\doit\새파일.txt",'w')
for i in range(1,11):
    data ="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
#
f= open("C:\doit\새파일.txt",'r')
line=f.readline() # 라인 하나 읽기
print(line)
f.close()
# 라인 하나씩 읽어줌
f= open("C:\doit\새파일.txt",'r')
while True:
    line=f.readline() 
    if not line: break
    print(line)
f.close()
#전체 리스트로 반환 
f= open("C:\doit\새파일.txt",'r')
lines=f.readlines() # 다수 라인 리스트로
for line in lines:
    line= line.strip() #줄바꿈 삭제
    print(line)
f.close()
#문자열로 반환
f= open("C:\doit\새파일.txt",'r')
data=f.read()
print(data)
f.close()
#추가
f= open("C:\doit\새파일.txt",'a')
for i in range(11,20):
    data= "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
#
f = open("C:\doit\oo1.txt",'w')
f.write("Life is too short, you need python")
f.close
    #같음
with open("C:\doit\oo.txt",'w')as f:
    f.write("Life is too short, you need python")
#
f= open("C:\doit\dream1.txt","r")
contents =f.read()
print(contents)
f.close()
#
with open("C:\doit\dream1.txt","r") as f:
    print(f.read())
#
with open("C:\doit\dream1.txt","r")as f:
    contents =f.read()
    word_list = contents.split(" ")
    line_list = contents.split("\n")
print("총 글자의 수 :", len(contents))
print("총 단어의 수 :", len(word_list))
print("총 줄의 수 :", len(line_list))
##1
h=0
for i in range(1,101):

    if i%4==0:
        continue
    else:
        h+=i
print(h)
##2
def sum(a,b):
    for i in range(a,b+1):
        b+=i
    return b
sum(1,10)  
sum(1,100)
##3
def exp(a,b):
    a=a**b
    return a
exp(10,2)
##4

def mul(*a):
    result =1
    for i in a:
        result *=i
    return result
mul(1,23,2,3)



def add_mul(*a):
    result =1
    for i in a:
        result *=i
    return result
result = add_mul(1,2,3,4,5)
print(result)

###########오류 덩어리 지만 ㅁ
r=1
c=0
def mul(*a):
    for i in a:
        b=list(a)
    print(b)
    for j in b:
        c=b[j]
        print(c)
mul(4,56,23,456,8671,21)                 
   

