x = "     this is my laptop. dont touch this thing.       "
txt =x.strip()
print("This is me",txt,"MIne is black")
a = "ATIYA SANJIDAH FAIZA"
b= a.split()
print(b)
c= ".".join(b)
print(c)
import re
p = re.split(r'\s+', a)
print(p)
q= [word for word in x.split()]
r="%".join(x)
print(q)
print(r)
print(a.isupper())
print(x.islower())
print(a.lower())
print(x.upper())
k=x.replace("this", "popy")
print(k)
input = input("enter a sentence: ")
w=input.split()
print(len(w))