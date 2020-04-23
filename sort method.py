h = [2,1,3,9,13,32,22,12]
h.sort(key=lambda x:x%2==0)
print(h)
f = sorted(h, reverse=True)
k = sorted(h,key=lambda x: x % 2 ==0)
print(k)
print(f)
#min/max function
k=[2712,6,23]
o1=min(k)
o2=max(k)
print(o1,o2)
#2
k=['hello','abhinav','ravi','venky']
o1=min(k,key=lambda x:sum(list(map(ord,x))))
o2=max(k,key=lambda x:sum(ist(map(ord,x))))
print(o1)
print(o2)
import functools
k=[1,3,5,6,2]
out=functools.reduce(lambda x1,x2:x1-x2,k)
print(out)
