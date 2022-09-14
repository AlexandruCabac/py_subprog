def fact(x):
    p=1
    for i in range(1,x+1):
        p*=i
    return p
n=int(input())
m=int(input())
if(n>=m):
    print(fact(n)/(fact(m)*fact(n-m)))
else:
    print("erorr")