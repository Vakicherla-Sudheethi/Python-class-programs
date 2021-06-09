#program to positive or negative number
numb=int(input('enter a number: '))
if numb>0:
    print('positive')
elif numb<0:
    print('negitive')
else:
    print('neither positive or negative')
#minimization of same program
numb=int(input('enter a value: '))
if numb:
    if numb>0:
        print('+ve')
    else:
        print('-ve')
else:
    print('zero')
