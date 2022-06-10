import socket 
import sys 
import time
print("\nAravinth R - 19MIC0053")
s=socket.socket() 
host=input(str("\nEnter Host Name : ")) 
port=1234
def findPhi(p,q):
    phi=(p-1)*(q-1)
    return phi
def findD(e,phi):
    for i in range(1,phi):
        if((e%phi)*(i%phi)%phi==1):
            return i
p=int(input("\nEnter P : "))
q=int(input("\nEnter Q : "))
e=int(input("\nEnter E : "))
n=p*q
phi=findPhi(p,q)
d=findD(e,phi)

print(f"\nYour Public Key - ({e},{n})")
print(f"\nYour Private Key - ({d},{n})")
try:
    s.connect((host,port))
    print("\nConnected to Server !\n") 
except:
    print("\nConnection Failed !") 
while 1:
    incoming_msg = s.recv(1024) 
    incoming_msg = incoming_msg.decode()
    p=int(incoming_msg)
    p0=(p**e)%n
    p2=(p0**d)%n
    print("\n-------Server-------\n\nPlain Text = ",incoming_msg)

    print("\nEncrypted Text = ",p0) 
    print("\nDecrypted Text = ",p2)


    message=input(str("\nEnter your message : ")) 
    message=message.encode() 

    s.send(message)