a=float(input("enter your income per year in lakhs:"))
if(a<=500000):
     print("your not qualify of paying tax:")
elif(a<500000 and a>700000):
     print("your income tax is ",(0.05*a)/100)
elif(a<700000 and a>1000000):
     print("your income tax is ",(0.10*a)/100)
elif(a<1000000 and a>1500000):
     print("your income tax is ",(0.15*a)/100)
elif(a<1500000 and a>3000000):
     print("your income tax is ",(0.30*a)/100)
else:
     print("your income is equals to Pakistans GDP")
