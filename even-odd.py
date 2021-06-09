#different ways to check the number is even or odd
numb=int(input("enter a number: "))
if numb%2==0:
    print("even")
else:
    print("odd")
#same program by not using == operator
numb=int(input("enter a number "))
if numb%2:#any numb % gives odd numb
    print('odd')
else:
    print('even')
#same program by using not
numb=int(input('enter a number: '))
if not numb%2:#here not is used to say that if the condition is not true
    print('even')
else:
    print('odd')

