#
"i eat %d apples." %3
number =3
print(number+1);
" i eat %d apples." %3;
#
number=10;
day="three";
"I ate %d apples. so I was sick for %s days."%(number,day)
"I have %s apples" %3
#
"%0.4f" %3.42134234
"%10.4f" %3.42134234
#전체길이 10인 문자열 공간 hi 오른쪽 정렬
"%10s" %"hi"
#왼쪽 정렬
"%-10skane." % "hi";
#
name="홍길동"
age =30
#print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
#format
"I eat {0} apples".format(3)
#
a="to"
b="the"
"no one ready {0} die, even {1} sinners ".format(a,b)
#
number=3
day="three"
"I ate apples. so I was sick for {1} days." .format(number,day)
#
print("안녕하세요")
print(100)
print("100")
#
print("100+100")
print("%d"%(100+100))
#오류
print("%d"%(100,200))
print("%d %d"%(100))
#
print("%d/%d=%sf"%(100,200,0.5))
print("%d/%d=%.1f")%(100,200,0.5)
#
print("%d"%123)
print("%5d"%123)
print("%05d"%123)
#
print("%f"%123.45) 
print("%7.1f"%123.45) #반올림
print("%7.3f"%123.45)
#
print("%s"%"python")
print("%10s"%"python")#오른쪽 정렬(공백4)
######################################################################
print("%d %5d %05d" %(123,123,123))
print("{0:d} {1:5d} {2:05d}" .format(123,123,123))
print("{2:d} {1:d} {0:d} ".format(100,200,300))
#
print("한 행입니다. 또 한 행입니다.")
print("한 행입니다.\n 또 한 행입니다.")
#escape
print("\n줄바꿈\n연습")
print("\t탭\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print(" \\\\\\ 역슬래쉬 3개로 출력")
print(r"\n \t \" \\ 를 그대로 출력");
#1-1
a=int(input("당신 나이는 몇살?"))
print("제 나이는 %d입니다."%a );
#1-2
a=int(input("당신 나이는 몇살?"))
print("제 나이는 {0}입니다.".format(a) );
#2
name=input("당신의 이름은?")
print("%s 입니다"%name )
#3
print("제 나이는 {0}이고 이름은 {1}입니다.".format(a,name))
#
a=("hobby")
a.count("b")
v="python is best choice"
v.find("b")
v.find("k") #없으면 -1 반환
#
a="life is to short"
a.index('t')
a.index('k') #에러 메시지 반환
#대문자,소문자
a=","
a.join('abcd')
a="sMa"
a.upper()
a.lower()
#공백제거
a=" space "
a.strip()
# replace
a= "life is too short"
a.replace("life", "Your leg")
# split
a.split()
a="a:b:c:d"
a.split(":")
#우선순위
a,b,c=2,3,4
print(a+b-c,a+b*c,a*b/c)
(a+b)-c
a+(b-c)
#형변환
s1,s2,s3 = "100","100.123","99999999999999999999999"
print(int(s1)+1,float(s2)+1,int(s3)+1)
a=100,b=100.123
str(a)+'1',str(b)+'1'
#
a=10
a+=5; print(a)
a-=5; print(a)
a*=5; print(a)
a/=5; print(a)
a//=5; print(a)
a%=5; print(a)
a**=5; print(a)
##1
money,c500,c100,c50,c10=0,0,0,0,0
money=int(input("얼마 넣을것?"))
c500= money//500
money%=500
c100= money//100
money%=100
c50= money//50
money%=50
c10= money//10
money%=10
print("500원{0}개,100원{1}개,50원{2}개,10원{3}개 입니다 ".format(c500,c100,c50,c10))
##2
money,c50,c10,c5,c1=0,0,0,0,0
money=int(input("얼마 넣을것?"))
c50= money//50000
money%=50000
c10= money//10000
money%=10000
c5= money//5000
money%=5000
c1= money//1000
money%=1000
print("신사임당{0}장,세종대왕{1}장,이이{2}장,이황{3}장\n잔액은{4}원 입니다 ".format(c50,c10,c5,c1,money))
#list
odd=[1,3,5,7,9]
a=[]
b=[1,2,3]
c=['life','is','too','short']
d=[1,2,'life','is']
e=[1,2,['life','is']]
a=[1,2,3]
b=[4,5,6]
a+b
a*3
#list indexing
a=[1,2,3]
a[2]
a[0]+a[-1]
#list slicing
a=[1,2,3,4,5,6,7,8]
a[0:9:2]
#
a=[1,2,3,['a','b','c']]
a[3][0]
a[-1][-1]
#######################################################################
a=[1,2,['a','b',['life','is']]]
a[-1][-1][0]
a[-1][1]
# 수정
a[1,2,4]
a[2]=3
a[1:2]=['a','b','c']
# 삭제
a=[1,'a','b','c',4]
a[1:3]=[]
del a[1]
a=[1,2,3,4,5]
del a[2:]
a.pop()
a.remove(4)
a.remove([7,8])
# 추가 
a=[1,3,4,2]
a.append(5) 
a.append([2,3])
a.append("b")
a.append([17,[8,9]])
a.extend([9,8,7,6])
a+[10]
# 정렬
a.sort()
a.reverse()
a.index([17,[8,9]])
#
a.insert(0,4)
a.count(2)
##1
colors=['red','blue','green']
print(colors[0],colors[-1],len(colors))
##2
string="python1"
print(string)
string[3:]
string[:3]
string[:4]
string[:-1]
##3
color1=['red','blue','green']
color2=['orange','black','white']
color1+color2
color1*2
color1+color2[:-1]
#tuple
t1=(1,2,'a','b')#튜플은 데이터 변결 불가
t1[0]
t1[1:]
#
t2=(3,4,5)
t1+t2
t2*3
len(t1+t2)
#list 필요성
#변수가 많을때
a,b,c,d=0,0,0,0
h=0
a= int(input("1st num:"))
b= int(input("2nd num:"))
c= int(input("3rd num:"))
d= int(input("4th num:"))
h=a+b+c+d
print("합계 %d"%h)
         #vs 
aa[0,0,0,0]       
h=0
aa[0]= int(input("1st num:"))
aa[1]= int(input("2nd num:"))
aa[2]= int(input("3rd num:"))
aa[3]= int(input("4th num:"))
h=aa[0]+aa[1]+aa[2]+aa[3]
print("합계 %d"%h);
# 
aa=[]
for i in range(0, 100):
    aa.append(0)
len(aa);

aa=[]
for i in range(0,4):
    aa.append(0)
h=0

for i in range(0,4):
    aa[i]= int(input(str(i+1)+"번째 숫자 :"))
h=aa[0]+aa[1]+aa[2]+aa[3]
print(h)
# 블록 설정후  ctrl + enter
#dictionary
dic={'name':'pey','phone':'0119993323','birth':'1118'}
a={1:'a'}        
a[2]='b'
a['name']='pey'
a[3]=[1,2,3]
del a[1]#삭제할때  key를 통해서 삭제한다
grade={'pey':10,'juliet':99}
grade['pey'+'juliet']# KEY 에러 남. 동시출력 불가
grade['juliet']
# 중복키값 ㄴㄴ
a={1:"a",1:"b"}
#
dic={'name':'pey','phone':'0119993323','birth':'1118'}
dic.keys()
dic.values()
dic.items()
for i in dic.keys():
    print(i) 
for j in dic.values():
    print(j)
for k in dic.items():
    print(k)
dic.clear() # 비우기
#key 로 value 얻기
dic.get('birth')
'name' in dic
#집합 자료형_중복과 순서 없다.
s1=set([1,2,3])
s1
s2=set("Helloamigo")
s2
#
s3=set([1,2,3,4,5,6])
s4=set([4,5,6,7,8,9])
s3&s4  
s3.intersection(s4)
s3|s4
s3.union(s4)
s3-s4
s3.difference(s4)
# set -> list, tuple 
s1=set([1,2,3])
l1=list(s1)
l1
t1=tuple(s1)
t1
#
s1=set([1,2,3])
s1.add(7) #하나 추가
s1.updata([4,5,6]) #다수 추가
s1
s1.remove(2)
s1
#
a=[1,2,3,4]
while a:
    print(a)
    print(a.pop())
#boolean
a=True
b=False
type(a)
3>23

#힐당연산자(assignment)  '='
a=1
b="python"
c=[1,2,3]

#########################################################################################################
#연습문제
##1
b={"국어":80,"영어":75,"수학":55}
d=list(b.values())
avg_b=(d[0]+d[1]+d[2])/3
print(avg_b)
##2
n=int(input("숫자"))
if (n%2==0):
    print("짝수")
else:
    print("홀수")
##3
pin="881120-1068234"
yyyymmdd =list(pin)
num =yyyymmdd[0:6]+yyyymmdd[7:14]
print(num[0:6])
print(num[6:13])
##4
yyyymmdd[7]
##5
a="a:b:c:d"
b=a.replace(':','#')
b
##6
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
##7
a=['life','is','too','short']
b=' '
result=b.join(a)
print(result)
##8
a=(1,2,3)
a=list(a)
a.append(4)
a=tuple(a)
print(a)
##9
a=dict()
a[('name')]='yor'
a[('a',)]="yor"
a[[1]]='yor' #오류 unhashable type: 'list'
a[250]='yor'
##10
a={ 'A':90,'B':80,'C':70}
a=list(a.items())
result=a.pop(1)# a[1][-1]
print(a)
print(result)
##11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)
##12
#리스트->포인터의 성질 가짐
a=[1,2,3]
b=a
a[1]=4
print(a,b)
print(id(a),id(b)) #값을 가져오려면 복사하면 원본도 바쒼다. 주소참조 때문.. 그래서 슬라이싱으로 가져온다
c=a[:]
a[1]=5
print(a,c)
