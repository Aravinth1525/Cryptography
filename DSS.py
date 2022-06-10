def findPhi(p,q):
    phi=(p-1)*(q-1)
    return phi
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m
p=int(input("\nEnter P : "))
q=int(input("\nEnter Q : "))
e=int(input("\nEnter E : "))
n=p*q
print("\nn (p*q) -",n)

phi=findPhi(p,q)
print("\nPhi(n) -",phi)

d=modinv(e,phi)
print("\nd -",d)
print(f"\nYour Public Key - ({e},{n})")
print(f"\nYour Private Key - ({d},{n})")

msg = int(input("\nEnter the message to encrypt : "))
    
r=(pow(msg,d))%n
print("\nYour Encrypted Message : ",r)
print()
r1=(pow(r,e))%n
print("Your Decrypted Message : ",r1)
print()
if(msg==r1):
    print("Message Accepted !")
    print()
else:
    print("Message not Accepted !")
    print()

    

    