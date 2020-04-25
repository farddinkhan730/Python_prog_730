                                    # 1->program to find the power of numbers using annonymous function
my_list = list(map(int,input()))
out = lambda x: x ** 2 ,my_list
print(out)


                                                        # or
my_list = list(map(lambda x : x ** 2 ,map(int,input())))
print( my_list)



                                                         #or
my_ist = int(input())
res = list(map(lambda x : x ** 2,range(my_ist)))
for i in range(my_ist) :
    print("2 of a numbers is",i,"->",res[i])



                                    #2-> Program to find the square of 2 using annonymous function
my_list = list(map(lambda x : 2 ** x,map(int,input())))
print(my_list) #output




                                                        #or
my_ist = int(input())
res = list(map(lambda x: 2 ** x,range(my_ist)))
for i in range(my_ist) :
    print("2 of a numbers is",i,"->",res[i])






                                    #3-> Program to find number divisible by onother number
                                                #-> Prog using lamba function
n = int(input("Enter the number to find the divisible numbers"))
m = int(input("Enter the range"))
out=list(map(lambda x : x % n == 0 ,range(m)))
res=[]
for i in range(1,m):
    p=out[i]
    if p==True :
        res.append(p)
    else :
        pass
print(res)




                                                     #or
                                        #->prog without using function
n = int(input("Enter the number to find the divisible numbers"))
m = int(input("Enter the range"))
res=[]
for i in range(1,m):
    if n % i == 0 :
        res.append(i)
    else :
        pass
print(res)




                                                     #or
                                     #->prog  without using lambda function
def div(x,y) :
    if x % y == 0 :
        res.append(y)
    else :
        pass
n=int(input("Enter the number to find the divisibl"))
m=int(input('enter the range upto which divisible find'))
res=[]
for i in range(1,m):
    div(n,i)
print(res)
print("END")
                            #4-> prog to find numbers divisible by 13
my_list = [12, 65, 54, 39, 102, 339, 221,]


result = list(filter(lambda x: (x % 13 == 0), my_list))


print("Numbers divisible by 13 are",result)
                            #5-> Prog to  find HCF or GCD
def gcd_hcf(x,y) :
    if x>y :
        return gcd_hcf(x-y,y)
    elif x<y :
        return gcd_hcf(x,y-x)
    else :
        return x
out=gcd_hcf(int(input()),int(input()))
print(out)
                            #           OR
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = 54
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))
                        #               OR
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)

