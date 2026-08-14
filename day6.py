def fun():
    print("Atiya Sanjida faiza")
fun()
def evod(x):
    if (x%2==0):
        return "even"
    else:
        return "odd"
print(evod(17))
def myfun(x,y=50):
    print(x)
    print(y)
myfun(10,40)
myfun(10)
def stud(fname, lname):
    print(fname, lname)
stud(fname='Atiya', lname='sanjidah')
stud(lname='Sanjidah', fname='atiya')
def nameage(name, age):
    print("I am ", name)
    print("My age is", age)
print("1.")
nameage("faiza",22)
print("2")
nameage(22, "faiza")
def myarbit(*args, **kwargs):
    for arg in args:
        print(arg)
    print("kwargs")
    for key, value in kwargs.items():
     print(f"{key}=={value}")
myarbit('hey','those','are','mine',first ='the chair', second='the book')
def f1():
    s="I love myself "
    def f2():
         print(s)
    f2()
f1()
def sqvalue(x):
   
        return x**2
print(sqvalue(2))
print(sqvalue(-16))
def passfun(x):
    x[0]=20
b=[10,11,12,13]
passfun(b)
print(b)
def  passfun2(x):
    x=20
a=10
passfun2(a)
print(a)
def show():
    print("Diba is equal to magic")
func =show()
x=123
def display():
    x=98
    print(x)
    print(globals()['x'])
print(x)
a= display
a()
j="atiya sanjidah faiza"
upper = lambda x: x.upper()
print(upper(j))
check = lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
print(check(15))
print(check(-9))
print(check(0))
func = [lambda arg = x : arg * 10 for x in range(1,5)]
for i in func:
    print(i()) 
cal = lambda x, y: (x+y, x*y)
res = cal(100, 80)
print(res)

even = filter( lambda x:x%2==0, b)
print(list(even))
doub = map(lambda x:x*2, b)
print(list(doub))
from functools import reduce
mul = reduce(lambda x,y:x*y, b)
print(mul)
def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(65))
file = open("file.txt","r")
content = file.read()
print(content)
with open("file.txt","r") as i:
    print(i.read())
fi = open("file.txt","r") 
for line in fi:
    print(line.strip())
fi.close()

line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()
image = open("ex.png","rb") 
cont = image.read()
print(cont)
image.close()
import csv
import io
csv_data = """Year, Name, ID
             2004,  Faiza, 12
             2018,  Unaisa, 15
             2015,  Kaisan, 16"""
csvfile = io.StringIO(csv_data)
csvreader =csv.reader(csvfile)
for row in csvreader:
    print(row)
import json
with open("json.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)
with open("file.txt","w",encoding="utf-8") as f:
    f.write("Created uisng mode.\n")
    f.write("2nd line\n")
with open("file.txt","r",encoding="utf-8" ) as f:
    print(f.read())
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())
try:
 with open("file.txt", "x", encoding="utf-8") as f:
    f.write("Exclusive mode.\n")
except FileExistsError:
  print("This file exists")
try:
 with open("faiza.txt", "x", encoding="utf-8") as f:
    f.write("Exclusive mode.\n")
except FileExistsError:
  print("This file exists")
lines = ["I am using multiple line.\n", "this method is easy.\n", "I would like to use this more\n"]
with open("faiza.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("faiza.txt", "r", encoding="utf-8") as f:
    print(f.read())
data = b'\x00\x01\x02\x03\x04'
with open("file.bin", "wb") as f:
    f.write(data)
with open("file.bin", "rb") as f:
    print(f.read())
from pathlib import Path
Path("faiza.txt").write_text("welcome to my world\n")
content = Path("faiza.txt").read_text()
print(content)