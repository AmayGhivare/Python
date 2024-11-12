#simple calculator

a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=str(input('select operator'))
if (c=='+'):
    print(a+b)
elif (c=='-'):
    print (a-b) 
elif (c=='*'):
    print(a*b)
elif (c=='/'):
    print (a/b)
elif (c=='%'):
    print(a%b)
else:
    print("worng operator")