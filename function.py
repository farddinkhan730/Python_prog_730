                            #global variables

def my_function():
    print("x inside :", x)
x='global'
my_function()
print("x outside:", x)
                        #local variables

def my_fun():
    y='local'
    print("y inside",y)
my_fun()
print("y outside",y)

                         # global and local
# 1
i = "global"
def function():
    global i
    y = "local"
    i = i * 2
    print(i)
    print(y)
function()
print(i)
# 2
x =5
def fun():
    x = 10
    print("local x:",x)
fun()
print("global x:",x)
                        # Lambda function
#1
l=[1,2,3,45,23,12,11,13,10]
k=list(map(lambda x: x % 2 ==0,l))
print("old list ",l)
print(f"new list {k}") #output [false,true,false,false,false,true,false,false,true]
#2
l=[1,2,3,45,23,12,11,13,10]
k=list(filter(lambda x: x % 2 ==0,l))
print("old list ",l)
print(f"new list {k}") #output [2,12,10]
#3
def xyz():
    if x % 2 == 0 :
        k.append(i)
x=[34,22,12,13,45,34]
k=[]
for i in x:
    xyz(i)
print(k)
#4
def intersection(a,b):
    res = []
    for i in a:
       if i in b:
            res.append(i)
    print(res)
x=input().split(" ")
y=input().split(" ")
intersection(x,y)
print(x,y)
