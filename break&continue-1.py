#break and continue statements
#eg-1
num=int(input())
i=1
while i<=num:
    #here based on the condition of the loop is called natural breaking
    #break-here used -then it print only "Hai"
    print(i,end=" ")
    break
#break-gets out of the loop
print("Hai")
#eg-2
#at a particular point it reaches and breaks
n=int(input())
l=1
while l<=n:
    print(l,end=" ")
    l+=1
    if i==5:
        break
print("hello")
