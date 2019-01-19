#Normal & lambda function in python

def double(n):
    return n*2

double_lambda = lambda n: n*2

#print(double(5))
#print(double_lambda(6))

#Classes in Python

#pass keyword to be used in python

class pyname:
    pass

name = pyname()
#print(name)

x=[[1,2],[3,4],[5,6]]
for i in x:
    print(i)

print("Transpose")

y=[]
z=[]
for i in x:
    y.append(i[0])
    z.append(i[1])

print(y)
print(z)

