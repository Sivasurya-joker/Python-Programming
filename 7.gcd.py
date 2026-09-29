def GCD (x,y):
 rem=x%y
 
if(rem==0):
     return y
else:
     return GCD(y,rem)

n = int (input("Enter the number:"))
m = int (input("Enter the secont number:"))

print (" The GCD of the two num is ",GCD(n,m))

