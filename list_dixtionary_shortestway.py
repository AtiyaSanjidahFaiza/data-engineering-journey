numbers = [1, 2, 3, 4, 50,90,6,58,260]
squares = [x * x for x in numbers]
print(squares)
even = [x for x in numbers if x%2==0]
print(even)
gt = [x for x in numbers if x>50]
print(gt)
names = ["John", "Sara", "Alex",]
students = {i: name for i, name in enumerate(names, 1)}
print(students)
nam = input("Enter names: ").split()
cgpa = input("enter CGPA: ").split()
for i, (nam,cgpa) in enumerate(zip(nam,cgpa), 1):
    print(i, nam, cgpa)
s={x:x*x for x in numbers}
print(s)

