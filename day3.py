import random
num = 0
while num<10:
    print("me")
    num=num+2
#annying while loop
#name=" "
#while name != "your name":
    #print("please enter your name \n")
   # name= input()
#print("thank you")
#while True:
   # print('Please type your name.')
    #name = input()
    #if name == 'your name':
      #continue
#print#('Thank you!')
###if n != "unaisa":
   #     continue
    #n2= input("password: ")
   # if n2 == "numberblocks":
    #       break
#print("Access granted")
while num<60:
     print(num)
     num=num+1
else:
     print("its is no longer 60")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for y in range(5, -1, -1):
    print(y)
    print("random: ")
for y in range(5):
    print(random.randint(1,10))
#multiplication table
n2=int(input("enter a number: "))
for i in range(1,11):
    print(n2, "x ",i,"=", n2*i )
#sum of numbers
for i in range(1,11):
    sum= n2+i
    print(sum)
#Factorial
factorial=1
for i in range(1,n2+1):
    factorial=factorial*i
    print(factorial)
#fibonacci series:
a=0
b=1
for i in range(n2):
    print(a)
    c=a+b
    a=b
    b=c
#prime number
if n2<=1:
    print("not prime ")
else:
    is_prime=True
    for i in range(2,n2):
        if n2%i==0:
            is_prime= False
            break

    if is_prime:
        print("prime number ")
    else:
        print("not prime number ")
