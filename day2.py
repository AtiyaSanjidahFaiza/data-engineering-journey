name ="faiza"
print(name)
print(len(name))
#spam = input()
#int(1.2)+1
a=12
b=2
#arithmatic
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
p=True
q=False
print(a<=18 and a!=p)
#Even or odd
num1, num2 =map(int,input("enter 2 numbers ").split())
if(num1%2==0):
    print(+num1," is even number")
else:  
    print(+num1," is odd number") 
#Voting
if(num2>=18):
    print("this person can vote cause the age is ",num2)
else:
    print("this person cannot vote cause the age is ",num2)
#grade calculator
m= int(input("Enter your number "))
if(m>=90 and m<=100):
    print("A+")

elif(m>=80 and m<=89):
    print("A")
elif(m>=70 and m<=79):
    print("A-")
elif(m>=60 and m<=69):
    print("B+")
elif(m>=50 and m<=59):
    print("B")
elif(m>=40 and m<=49):
    print("B-")
else:
    print("F")

#largest of three numbers
k, l, n =map(int,input("enter 3 numbers").split())
max_ = k
if(l>k and l>n):
    max_=l
    print(l)
elif(n>k and n>l):
    max_=n
    print(n)
else:
    print(k)



