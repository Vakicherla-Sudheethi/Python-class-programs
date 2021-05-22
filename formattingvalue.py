"""%s-for formatting string value
%d=integer
%f=float
%o=octal
%c=character
%x=hex value for lower case
%X=hex value for uppercase"""

name="cse-a"#for string
print("hello %s!how are you?"%(name))
age=19#for integer value
print("age is %d" %(age))
#combining the %s & %d
print("hello %s! your age is %d"%(name,age))
percentage=8.6
print("my percentage is %f"%(percentage))
# for three formats in a single line
print("hello i am %s my age is %d and my percentage is %f"%(name,age,percentage))
#formatting of X hex
o=16
print("Number is %X"%(o))
#formatting of octal
p=7
print("Number is %o"%(p))
#formatting of character
i="h"
print("the character is %c"%(i))
