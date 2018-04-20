import helloworld #Import Helloworld attribs in new world

first = helloworld.string1
second = "New World"

way1="A sentence with {0} and {1}".format(first, second)
way2 = f"A sentence with {first} and {second}"

#print(way1)
#print(way2)

def pnt(first, *second):
    print(first)
    print(second[1])


pnt("Hwllo","akshd","asjdsakd","asjdhaskjd")