n=int(input())
m=int(input())
def sum_n(x,y): return x+y
def pro_n(x,y): return x*y
def med_n(x,y): return (x+y)/2
def cmmdc(x,y):
    b=0;
    v=max_n(x,y)
    q=min_n(x,y) 
    while(b==0):
        if((v==q) or v<q):
            b=1
        else:
            v-=q
    return v
def cmmmc(x,y): return (x*y)//cmmdc(x,y)
def min_n(x,y): return x if x<y else y
def max_n(x,y): return x if x>y else y
def sum():
    a=int(input())
    b=int(input())
    print(a,"+",b,"=",a+b)
def pro():
    a=int(input())
    b=int(input())
    print(a,"*",b,"=",a*b)
def divis(x,y):
    loc=[]
    for i in range(1,int(x/2)+1 if x<y else int(y/2)+1):
        if(x%i==0 and y%i==0):loc.append(i)
    if(max_n(x,y)%min_n(x,y)==0):    
        loc.append(min_n(x,y))
    return loc
def multi(x,y):
    loc=[]
    a=cmmmc(x,y)
    for i in range(1,6):
        b=a*i
        loc.append(b)
    return loc
def c_com(x,y):
    loc=""
    for i in "0123456789":
        if(i in str(x) and i in str(y)):
            loc+=i
    return loc
def c_sep(x,y):
    loc=""
    for i in "0123456789":
        if(i in str(x) and i not in str(y)):
            loc+=i
    return loc
def fr(x,y):
    a,b=0,0
    for i in range(1,int(x/2)+1):
        if(x%i==0):
            a+=1
    for i in range(1,int(y/2)+1):
        if(y%i==0):
            b+=1
    if a==b: print("PRIETENE")
print(sum_n(n,m),pro_n(n,m),med_n(n,m),cmmdc(n,m),sep='\n')
print(cmmmc(n,m),min_n(n,m),max_n(n,m),sep='\n')
sum(),pro()
print(divis(n,m),multi(n,m),c_com(n,m),c_sep(n,m),sep='\n')
fr(n,m)