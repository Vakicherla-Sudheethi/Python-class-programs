#Scope variables
"""local variable--global variable"""
s=int(input("enter number: "))#global variable
def factorial(num):
    fact=1#local variable and scope is limited to factor
    for i in range (1,num+1):
        fact=fact*i
    print("fact of %d is %d "%(s,fact))#s is global is used
#call the function
factorial(s)
"""output:enter number: 5
fact of 5 is 120"""        
