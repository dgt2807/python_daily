#모듈 함수,변수,클래스 모아 놓은 파일
#1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
                            #접시행할 경우 참이여서 돌아간다.import하면 거짓으로 실행안됨
if __name__=="__main__":    #print문의 실행을 선택적으로 막는 것 JU03F[line208]
    print(add(1,4))         
    print(sub(4,2))

#2
def func1():
    print("Module1.py의 func1()이 호출됨")

def func2():
    print("Module1.py의 func2()이 호출됨")
    
def func3():
    print("Module1.py의 func3()이 호출됨")

#3
PI =3.141592
class Math:
    def solv(self,r):
        return PI*(r**2)
def sum(a,b):
    return a+b

if __name__=="__main__":
    print(PI)
    a=Math()
    print(a.solv(2))
    #print(sum(PI,4.4))    