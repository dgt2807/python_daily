coffee=10
while True:
        money= int(input(" money"))
        if money ==300:
            print("wait for minute")
            coffee-=1
        elif money>300:
            print("%d$ left, take it"%(money-300))
            coffee-=1
        else:
            print("get the coin ")
            print("amount of coffee is %d"%coffee)
        if coffee==0:
            print("soldout")
            break

 #C:\Users\A> cd c:\doit       
# c:\doit> python coffee.py        
