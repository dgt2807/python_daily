#if
money=0#1
if money:
    print("taxi")
else:
    print("bus")
#
a=99
if a<100:
    print("작아")
#
a=200
if a<100:
    print("작아")
print("보임")
print("끝")
#
x =3
y=2
x>y
x<y
x==y
x!=y
#
money=2000
if money >=3000:
    print("taxi")
else:
    print("walk")
#
print("tell me your age?")
myage=int(input())
if myage <30:
    print("welcome to the marching band")
else:
    print("access denied")
#
a= int(input("number"))
if a%2==0 :
    print("evennum")
else:
    print("oddnum")
#
money =2000
card =1
if money >= 3000 or card:
    print("taxi")
else:
    print("by foot")
##1
w=float(input("짐 무게 측정"))
if w >20:
    print("무거운 짐은 20,000원을 내셔야 합니다")
else:
    print("수수료는 없습니다")
print("감사합니다")    
##2
t=-10.05
if t>=30:
    print("반바지 입는 것을 권고")
else:
    print("긴바지를 추천")
print("환복을 완료했다면 나가서 운동")
#
ba=[1,2,3]
1 in ba
'a' in ba
tuple(ba)
'a' in ba
'j' not in ba
#
pocket=['spadea','a heart','money']
if 'money' in pocket:
    print("get a taxi")
else:
    print("walk")
#
pocket=['money','card','identification']
if 'card' not in pocket:
    print("walk")
else:
    print("ride a bus")
#pass
pocket=['money','card','identification']
if 'card' not in pocket:
    pass
else:
    print("buy one")
#
pocket=['paper','phone']
card = True
if 'money' in pocket:
    print("Taxi")
else:
    if card:
        print("get on the bus")
    else:
        print("walk")
#
a=75
if a>50:
    if a<100:
        print("less then 100 but more then 50")
    else:
        print("more then 100")
else:
    print("less then 50")
#
pocket=['paper','cellphone']
card =1
if 'money' in pocket:
    print("Taxi")
elif card:
    print("Taxi")
else:
    print("call anyone who could help")
#  100이상 점수 문제
score=int(input("score"))
print("Grade")
if score >=90 :
    if score >100:
        print("F")
    else:
        print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")    
#
by=int(input("생년:"))
age=2022-by+1
if age>=20:
    if age <=26:
        print("college")
    else: 
        print("not a student")
elif age>=17 :
    print("high school")
elif age>=14 :
    print("middle school")
elif age>=8 :
    print("elementry school")
else:
    print("not a student")
# if 20<=age <27 이면 됨 근데 and or 는 다음 elif에 영향 넘어감
score=10
message ="success" if score >= 60 else "failure"# 조건이 참인 경우 if 조건문 else 조건문 거짓인 경우 (삼항연산자)
message
        # 위와 같은 내용
if score >=60:
    message ="success"
else:
    message="failure"
        #삼항연산
res="합격" if score>=60 else"불합격"
res    
#while
treeHit = 0
while treeHit <10:
    treeHit =treeHit +1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit ==10:
        print("나무를 넘어갑니다.")
#
ab=0
while ab <1001:
    ab+=1
    print("while문 돌리는중")
#
i,s=0,0
i=1
while i<1001:
    s+=i
    print(i,s)
    print("1에서 %d 까지의 합계:%d "%(i,s))    
    i+=1#언제 print하냐 따라 달라짐 결과    
#
s,a,b,=0,0,0
while True:
    a = int(input("더할 첫째 수"))
    if a==0:
        break
    b = int(input("더할 둘째 수"))
    s= a+b
    print("%d+%d=%d"%(a,b,s))
#
coffee=10
money=300
while money:
    print("커피드림")
    coffee-=1
    print("남은 커피의 양은 %d개"%coffee)
    if not coffee:
        print("전량판매")
        break
#continue
a=0 
while a< 10:
    a+=1
    if a %2 ==0: continue  #짝수이면 conntinue를 타고 while절 시작지점으로 간다.(원래의 진행방향으로 가게 끔하는것)
    print(a)
##1
a=0
while a<10:
    a+=1
    if a %5==0:
        print(a)
#  무한루프      
while True:
    a*=9999999999999999999999999
    print(a)    
#for
test_list=['one','two','three']
for i in test_list:
    print(i)
#
a=[(1,2),(3,4),(5,6)] 
for (first,last)in a:
    print(first+last)
#
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number +=1
    if mark >=60:
        print("%d번 학생은 합격"%number)
    else:
        print("%d번 학생은 불합격"%number)
#
number =0
for mark in marks:
    number+=1
    if mark < 60: continue  #첨자엔 marks가 생으로 못 들어간다 makr로 변환
    print("%d번 학생은 합격"%number)
#range
summ = 0
for i in range(1,11):
    summ+=i
print(summ)
#
name=["철수","영희","길동","유신"]
for i in name:
    print("안녕!"+i)# 첨자를 넣어서 해결
#
summ=0
for i in range(1,101):
        summ+=i
print(summ)
#
for i in range(0,909,9):
    print("%d"%i) 
#
for i in range(2,-1,-1):
    print("%d"%i)       
#
for i in range(1,6,1):
    print("%d"%i,end=" ")       
#
a=0    
while a<6:
    print("%d"%a,end=" ")
    a+=1
#
i,h=0,0
for i in range(501,1001,2):
    h+=i
    print("%d,%d"%(i,h))
#
i,h=1,0
for i in range(-0,101,1):
    if i%7==0:
        print(i)
        h=i+h 
print("합은 %d"%h)
#
i,hap=0,0
num=0
num=int(input("입력"))
for i in range(1,num+1,1):
    hap+=i
print("합계 %d"%hap)
#
s=int(input("시작값을 입력"))
e=int(input("끝값을 입력"))
b=int(input("증가값 입력"))
h,i=0,0
for i in range(s,e+1,b):
    h+=i   
print("%d"%h)
#
i,dan=0,0
dan=int(input("단을 입력하세요:"))
for i in range(1,10,1):
    print("%d X %d=%2d"%(dan,i,dan*i))         
# 중첩
for i in range(0,3,1,):
    for j in range(0,2,1):
        print("i:%d,j:%d"%(i,j))
#
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print(" ")
#
a=[1,2,3,4]
result=[] 
for num in a:
    result.append(num*3)
print(result)

result=[num*3 for num in a if num %2 ==0]
print(result)
#
result =[x*y for x in range(2,10)
    for y in range(1,10)]
result
##1
p=int(input("구입할 금액을 입력하세요"))
if p>100000:
    s=(p-100000)*0.05
    p-=s
else:
    print("지불금액 %d"%p)
print("지불금액%d"%p)
##2
while True:
    a=int(input("달 입력"))
    if a<=12:   #짝수이면 conntinue를 타고 while절 시작지점으로 간다.(원래의 진행방향으로 가게 끔하는것)
        if a==2: print("28days")
        elif a in(4,6,10): print("30days")  
        else: print("31days")
        break

m1=int(input("month"))     
if m1==2:
    print("28days")
elif m1==4 or m1==6 or m1==10: # elif m1 in(4,6,10):  남의 아이디어
    print("30days")
elif m1<12: 
    print("31days")

##3
wd=("i like you")
w=list(wd)
w.reverse()
for i in w:
    print("%s"%i,end=" ")    


# 개쩌네     순간만 리스트 취급 하는 방법
b = "I like you"
for i in range (9, -1, -1) :
    print(b[i], end="")

# 개쩌네 2  순서를 이용한 방법 
s = ' '
a = input("입력:")
for i in a:
    s = i + s
    print(i)
    print(s)
print(s)    
    

##4
i=int(input("num"))
for i in range(i,1,-1):
    for j in range(9,0,-1):
        print("%d x %d =%d"%(i,j,i*j))
        