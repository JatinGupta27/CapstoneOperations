import addi
import sub
import sys

print("Enter the operation to perform")
print("1: Addition\n 2: Subtraction ")
inp = input()

print("Enter the values")
i1 = input("A:")
i2 = input("B:")

if (inp==1):
        addi.add(i1,i2)
if (inp==2):
        sub.subtract(i1,i2)
#else:
 #       print("Please select between 1 to 2 only")
  #      sys.exit(0)      
        
	
