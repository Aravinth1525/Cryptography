import socket 
import sys 
import time
print("\nAravinth R - 19MIC0053") 
s=socket.socket() 
host=socket.gethostname() 
print("\nServer will start on host : ",host) 
port=1234
s.bind((host,port))
print("\nServer is bound successfully\n") 
s.listen(1) 
connection,address=s.accept() 
print(address," has connected !")
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



while 1:
    message=input(str("\nEnter your message : ")) 
    message=message.encode()
    connection.send(message) 
    incoming_msg=connection.recv(1024) 
    incoming_msg=incoming_msg.decode() 
    p1=int(incoming_msg)
    p2=(p1**e)%n

    p3=(p2**d)%n

    print("\n-------Client-------\n\nPlain Text = ",incoming_msg)

    print("\nEncrypted Text = ",p2)
    print("\nDecrypted Text = ",p3)



