#if-else examples
#eg1-print the given number is positive or not
numb=int(input("enter a numb: "))
if numb>0:
    print("positive numb")
else:
    print("negative number")
#eg2-the character is vowel or consonant
o=input("enter a character: ")
if((o=='a')or(o=='e')or(o=='i')or(o=='o')or(o=='u')):
    print("vowel")
else:
    print("consonant")
#eg3-program to check profit or loss
cp=int(input("enter costing price: "))
sp=int(input("enter selling price: "))
if cp>sp:
    print("profit")
else:
    print("loss")
#eg4-the given char is upper or lower case
alphabet=input("enter a alphabet: ")
if (alphabet.islower()):
    print("lower case")
else:
    print("upper case")
