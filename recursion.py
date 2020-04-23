#1 factorial using recursion
def fact(x):
    p = 1
    if x == 0 :
        return p
    else :
        p = x*fact(x-1)
        return p
num = int(input("enter the number"))
out = fact(num)
print(out)

# 2 find th min square in rectangle
def min_sqr(r,w,c=0) :
    if r > w:
        c+=1
        return min_sqr(r-w,w,c)
    elif r < w :
        c+=1
        return min_sqr(w-r,r,c)
    else :
        return c+=1
out = min_sqr(5,2)
print(out)

#3 countdown
import time
def countdown(x):  # x = 4
    if x == 0:
        pass
    else:
        print(x)
        countdown(x-1)

v1 = time.time()
countdown(10)
v2 = time.time()
print(v2-v1)
print('Happy Recursion Day')
out1 = 0.014958620071411133

# countdown using iteration
def countdown(x):  # x = 4
    for  i in range(x, 0, -1):
        print(i)


v1 = time.time()
countdown(1000)
v2 = time.time()
print(v2-v1)
out2 = 0.011011362075805664

print(out1-out2)


