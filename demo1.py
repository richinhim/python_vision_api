
#coding:euc-kr
print ("Hello Python")


marks = [90,70,48,80]

number = 0

for mark in marks:
    number = number + 1

    if mark >= 60:
        print("%d pass" % number)
    else:
        print("%d no pass" % number)

def sum(a,b):
    return a + b

print(sum(1,2))

def f(i, mylist):
    pass
