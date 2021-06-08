#if-condition examples
#example 1
n=18
if n==18:
    print("True")
#eg 2-to check the given alphabet is vowel or not
o=input("enter the alphabet: ")
if((o=='a')or(o=='e')or(o=='i')or(o=='o')or(o=='u')):
    print("vowel")
#eg3 3-to check the number id less than 5.if <5 then print square of number
i=int(input("enter a number: "))
if i<=5:
           print("less than 5",i*i)
#eg 4-to check the given number is divisible by 10 or not
p=int(input("enter a number: "))
if((p%10)==0):
    print("the number is divisible by 10")
#eg 5-coount the no.of 100/- note and return the no.of nnotes required
note=int(input("enter the amount: "))
n=note/100
if n>1:
    print("more than 100/- required")

  
