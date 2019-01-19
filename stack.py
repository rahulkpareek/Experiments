
import datetime

s=[]

for i in range(100, 0, -1):
    s.append(i)

n = len(s)

#selection
x = datetime.datetime.now()

for i in range(0,n):
    min = i
    for j in range(i+1, n):
        if s[j] < s[min]:
            min = j
    temp = s[i]
    s[i] = s[min]
    s[min] = temp

y = datetime.datetime.now()
# print(s)

s1=[]

for i in range(100, 0, -1):
    s1.append(i)

#insertion
a = datetime.datetime.now()
for i in range(1, n):
    j = i
    while (j > 0 and s1[j] < s1[j-1]):
        tmp = s1[j]
        s1[j] = s1[j-1]
        s1[j-1] = tmp
        j = j-1
b = datetime.datetime.now()


print(y.timestamp() - x.timestamp())
print(b.timestamp() - a.timestamp())

