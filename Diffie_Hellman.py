from random import randint

P=int(input("\nEnter P - "))
G=int(input("\nEnter G - "))	
a=int(input('\nThe Private Key a for User A - '))	
x = int(pow(G,a,P))
b=int(input('\nThe Private Key b for User B - '))
y = int(pow(G,b,P))
ka = int(pow(y,a,P))
kb = int(pow(x,b,P))
print('\nSecret key for the User A - %d'%(ka))
print('\nSecret Key for the User B - %d'%(kb))
print()

