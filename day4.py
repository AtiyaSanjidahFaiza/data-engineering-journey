from collections import deque
#lists
a=[1,2,3]
print(a)
b=["apple",3,3.5,True]
print(b)
c=list((1,2,3,'rose',4.5))
print(c)
d=[2]*10000
print(d)
print(c[3])
print(c[-1])
e=list("Faiza")
print(e)
a.append(4)
print(a)
a.insert(4,5)
print(a)
a.extend([6,7])
print(a)
a[1]=25
print(a)
a.remove(25)
print(a)
a.pop(4)
print(a)
del a[3]
print(a)
a.clear()
print(a)
for item in e:
    print(item)
#nested lists
f=[[1,2],[3,4]]
print(f[0])
print(f[1][0])
fruits=("apple", "banana", "Mango")
print(fruits)
tup= tuple("geeks")
print(tup)
h,g,t,q,r = tup
print(h)
print(g)
print(t)
print(q)
print(r)
tup1=(11,12,13,14,15)
tup2=("atiya","Sanjidah","faiza")
tup3=tup1+tup2
print(tup3)
print(tup3[5:])# start
print(tup3[::-1]) #backwards
print(tup3[4:8])
r1= reversed(tup3)
print(tuple(r1))
deq=deque(tup3)
deq.reverse(
)
rev=tuple(deq)
print(rev)
s={10,50,20,60,20}
print(s)
print(type(s))
print(set(tup3))
t=frozenset(["%","&","$","#",10])
print(t)
s.add(100)
print(s)
u=s.union(t)
print(u)
i=s.intersection(t)
print(i)
d=s.difference(t)
print(d)
s.clear()
print(s)
j={"name":"Faiza", "age": 22}
print(j)
data= dict(nam="Atiya", age=18)
print(data)
print(data["nam"])
print(j.get("age"))
data["age"]=8
data["nam"]="unaisa"
print(data)
del data["age"]
print(data)
print(data.pop("nam"))
print(data)
print(j.popitem())
print(j)
val=dict(x=40 ,y=100)
for key in val:
    print(key)
for value in val.values():
     print(value)
for key, value in val.items():
    print(key,value)
m={"person":
   {
       "name":"Fareta",
       "hobby": "TV"
   }}
print(m)
print(m.copy())
print(m.items())
print(m.keys())
print(m.values())
print(val.setdefault(key))
print(dict.fromkeys(val,"not here"))
sq={x: x**2 for x in range(0,5)}
print(sq)
keys =['a','b','c','d']
values=[1,2,3,4]
d={k:v for(k,v) in zip(keys,values)}
print(d)
z= {x:x**3 for x in range(10) if x**3%4==0}
ns="faiza"
res={x:{y:x+y for y in ns} for x in ns }
print(res)