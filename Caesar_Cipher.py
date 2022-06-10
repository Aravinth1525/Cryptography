def en(t,k):
    ct=""
    for i in range(len(t)):

        r=((ord(t[i])-ord('a')))
        c=(k+r)%26
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

def de(c,k):
    pt=""
    for i in range(len(c)):

        r=((ord(c[i])-ord('a')))
        f=(r-k)%26
        d=chr(f+ord('a'))
        pt+=d
    return pt

a=input().lower()

k=int(input())
b=en(a,k)
print(en(a,k).upper())
print(de(b,k).upper())