def en(t,k1,k2):
    ct=""
    for i in range(len(t)):
        r=(ord(t[i])-ord('a'))
        c=(k1*r+k2)%26
        d=chr(c+ord('a'))
        ct+=d
    return ct

def modinv(e,phi):
	i = 1
	while i:
		d = str((phi*i+1)/e).split(".")
		if(d[-1] == '0'):
			return int(d[0])
		else:
			i+=1

def de(c,k1,k2):
    pt=""
    for i in range(len(c)):
        a=modinv(k1,26)
        d=(ord(c[i])-ord('a')-k2)
        p=(a*d)%26
        pt+=chr(p+ord('a'))
    return pt

a=input().lower()

k1=int(input())
k2=int(input())
ct=en(a,k1,k2)
print(en(a,k1,k2).upper())

print(de(ct,k1,k2))