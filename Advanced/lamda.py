# lambda expressions
# lambda param: func(param)
# lambda param: manipulation(param)
# lambda param: action(param)
from functools import reduce
my_list = [1,2,3]
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item%2 !=0, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))

# make a list each item square  
mero_list = [4,5,6]
print(list(map(lambda item: item**2, mero_list)))

# sort a = [(0,2),(4,3),(10,-1),(9,9)]
a = [(0,2),(4,3),(10,-1),(9,9)]
a.sort(key= lambda x: x[1])
print(a)