def findPhi(p,q):
    phi=(p-1)*(q-1)
    return phi
def findD(phi,e):
	i = 1
	while i:
		d = str((phi*i+1)/e).split(".")
		if(d[-1] == '0'):
			return int(d[0])
		else:
			i+=1
p=int(input("\nEnter P : "))
q=int(input("\nEnter Q : "))
e=int(input("\nEnter E : "))
n=p*q
print("\nn (p*q) -",n)

phi=findPhi(p,q)
print("\nPhi(n) -",phi)

d=findD(phi,e)
print("\nd -",d)
print(f"\nYour Public Key - ({e},{n})")
print(f"\nYour Private Key - ({d},{n})")
print()

while(True):

    result =""
    choice =input("Enter\n\n1. Encrypt\n2. Decrypt\n3. Exit\n\nYour Choice : ")
    if choice == "1":
        msg = int(input("\nEnter the message to encrypt : "))
    
        r=(pow(msg,e))%n
        print("\nYour Encrypted Message : ",r)
        print()
        

    elif choice == "2":
        msg = int(input("\nEnter the message to decrypt : "))
        r=(pow(msg,d))%n

        print("\nYour Decrypted Message : ",r)
        print()

    elif choice=='3':
        print("\nThank You !\n")
        exit()
    else:
        print("\nEnter a valid choice !\n")

    