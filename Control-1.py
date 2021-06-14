#control statements -1
for i in range(10):
    print(i,end=" ")
    """in range there are always 3 values
       range(inner,upper,inc/dec)..here 10 is the upper bound
       then the default values are 0 and incerement becomes 1"""
    """any single value is upper value and inc/dec is always step count=1 by default"""
#to print all the values but not a ms
for j in range(10):
    print(j,end=" ")#prints from 0-9
#considering the lower and the upper bound
for  j in range(2,10):
    print(j,end=" ")#prints from 2-9
#modification of step count
for j in range(2,10,1):#by default the step count value is 1
    print(j,end=" ")#here it gives the same o/p from 2-9
#changing the step count value
for j in range(2,10,2):#step count incremented by 2
    print(j,end=" ")
#if we want the upper value also to be executed
for j in range(2,10+1,2):
    print(j,end=" ")

    
