p=int(input())
g=int(input())
d=int(input())
e=pow(g,d)%p
m=int(input())
from operator import mod
import random
a = 7
y1=pow(g,a)%p
y2=(m*(pow(e,a)))%p
print(y1)
print(y2)

def modinv(e,phi):
	i = 1
	while i:
		d = str((phi*i+1)/e).split(".")
		if(d[-1] == '0'):
			return int(d[0])
		else:
			i+=1

y3=int(pow(y1,d))

y4=modinv(y3,p)
pt=(y2*y4)%p

print(pt)

