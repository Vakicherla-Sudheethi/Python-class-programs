o=input('Enter a string as input:')
p={}#{} are used to define a dictionary.
for i in set(o):
    p[i]=o.count(i)#count() function returns the number of occurrences of a substring in the given string.
print(p)
