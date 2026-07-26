from datetime import date


name = "john"
age =90
print(name, age )
n1= input("enter number\n")
print(n1)
print("Hello world")
nam = input("enter your name ")
print(nam)
print("enter ")
#making an age calculator
today = date.today()
birth_year = int(input("enter your birth year: "))
print(+birth_year)
birth_month = int(input("enter your birth month: "))
birth_day = int(input("enter your birth day: "))
age=today.year-birth_year

if(today.month,today.day)<(birth_month,birth_day):
    age-=1

print("the age is " ,age, " year ")
# Rectangle area:
width, height = map(float, input("enter the width and height of a rectangular: ").split())
print(width, height)
area = width * height
print(area)
#Mini calculator
num1, num2 = map(int, input("enter 1st number\n").split())
print(num1, num2)
sum = num1 + num2
print("sum is ", sum)

sub = num1 - num2
print("subtraction is ", sub)
multi = num1 * num2
print("Multiplication  is ", multi)
div = num1 / num2
print(" division is ", div)
modulo = num1 % num2
print("modolus ", modulo)


