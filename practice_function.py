a, b = map(int,input("enter 2 numbers").split())
#adding 2 numbers
def sum(x, y):
    return(x+y) 

print(sum(a,b))
#Even odd checker
def EvenOrOdd(x):
    if(a%2==0):
        print("This number is even")
    else:
        print("This number is odd")
print(EvenOrOdd(a))
#Finding the largest number
def largeNumber(x,y):
    large =x
    if(y>large):
        large = y
        return large
    else:
        return x
print(largeNumber(a,b))
#Factorial
def factorial(y):
    fact =1
    for i in range(1,y+1):
        fact=fact*i
    return fact
print(factorial(b))
#Celcius to farenhite
def CalciusToFarenhite(x):
    far = (x*9/5)+32
    return far
print(CalciusToFarenhite(a))
    
    


