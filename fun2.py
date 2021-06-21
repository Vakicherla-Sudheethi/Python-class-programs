#function with parameters
def show(x):
    print("show()")
    print(x)
    print(type(x))
#call the show fun
show("python")#show function with string value
"""output:show()
python
<class 'str'>"""
show(10)#show function with integer
"""output:
10
<class 'int'>"""
show(10.990909)#show function with float
"""output:
10.990909
<class 'float'>"""
set1={1,2,4,5,6}
show(set1)#show() with set data structure
"""output:
{1, 2, 4, 5, 6}
<class 'set'>"""
list1=["python","flat","daa","co"]
show(list1)
"""output:['python', 'flat', 'daa', 'co']
<class 'list'>"""
dict1={'john':5231,'hema':6145,'rani':2102,'uday':3204}
show(dict1)
"""output:{'john': 5231, 'hema': 6145, 'rani': 2102, 'uday': 3204}
<class 'dict'>"""
tuple1=([1,2,3])
show(tuple1)
"""output:[1, 2, 3]
<class 'list'>"""


