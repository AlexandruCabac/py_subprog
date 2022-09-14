def ad(a,c,b,d):
    s=0
    s=(a*d+b*c)/(c*d)
    return s
def inm(a,c,b,d):
    p=0
    p=(a*b)/(c*d)
    return p
z=int(input())
x=int(input())
y=int(input())
w=int(input())
print(ad(z,x,y,w))
print(inm(z,x,y,w))