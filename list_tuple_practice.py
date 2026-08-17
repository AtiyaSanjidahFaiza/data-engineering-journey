# Finding Maximum
a=[1,15,11,88,78,99,5,50,64,12]
max = a[0]
for i in a:
    if i>max:
        max = i
print(max)
#Finding minimum
min = a[0]
for i in a:
    if i<min:
        min = i
print(min)
#Finding sum
sum=0
for i in a:
   sum=sum+i
print(sum)
#finding averge
avg=sum/len(a)
print(avg)
#ascending sort
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
#descending order
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[j],a[i]=a[i],a[j]
print(a)
b=[2,5,5,99,99,10,1,5,14]
new=[]
for i in b:
    if i not in new:
        new.append(i)
print(new)
