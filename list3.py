#append() and insert() functions
classes=['a','b','c']
print(classes)
classes.append("d")#adds element to last
classes.insert(1,"A")#inserting at particular index
print(classes)
branches=[]#empty  list
size=len(branches)#length of the list
print("length of branches list is %d"%(size))
#add elements to the empty list
#append()-append adds the element to the last
branches.append("cse")
branches.append("ece")
branches.append("civil")
#printing
print(branches)
#another method to add element at the particular index
#insert(index,obj)
branches.insert(2,"Mech")#adds the element to index 2
print(branches)#here it shifts to next index

