#continue-to skip any values
num=int(input())
i=1
while i<=num:#1<=10,
    continue#here it skips the remaining statements
#it goes into while loop again and works infinite loop
    print(i,end=" ")
    #continue - is placed here it prints infinite 1
    i+=1
#eg-1
n=int(input())
j=1
while j<=n:
    if j%3==0:
        j+=1
        continue
    print(j,end=" ")
    i+=1
