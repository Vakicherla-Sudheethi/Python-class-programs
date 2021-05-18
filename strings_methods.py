#string methods
str1="hello"
str2="python"
str3=str1+str2#concatination of strings
print(str3)
#finding the length of the given string using len()
s="Apple"
len(s)
print('length of s',len(s))
#accessing the characters
p="world"
print('the character from p is',p[0])#prints the value at the [0]index in the given string
#accessing the subset of characters from the given string
r="python programming"
print(r[2:11])
print(r[:4])#ending index
print(r[9:])#starting index
print(r[1:9])#returns the substring of characters from 1-8 excluding 9
#splitting of the given substrings using split()
str_data="good morning"
print(str_data.split(" "))
print(str_data.split(" , "))
print(str_data.split())#default
