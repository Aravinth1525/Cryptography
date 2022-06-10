a1,m1=map(int,input("\nEnter a1 and m1 : ").split())
a2,m2=map(int,input("\nEnter a2 and m2 : ").split())
a3,m3=map(int,input("\nEnter a3 and m3 : ").split())
M=m1*m2*m3
M1=M/m1
M2=M/m2
M3=M/m3
def inv(a,m):
    for i in range(1,m):
        if((a*i)%m==1):
            return i
M1inv=inv(M1,m1)
M2inv=inv(M2,m2)
M3inv=inv(M3,m3)
res=((a1*M1*M1inv)+(a2*M2*M2inv)+(a3*M3*M3inv))%M
print("\nResult",int(res))
print()