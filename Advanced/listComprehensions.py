# list,set,dictionary 
# without list comprehension
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# with list comprehension 
# for string
my_strlist = [char for char in 'hello']
print(my_list)
# for number
my_numberlist = [num for num in range(0,100)]
print(my_numberlist) 
# for square
my_squarelist = [num**2 for num in range(0,100)]
print(my_squarelist)
# for filter odd num 
my_EvenFilterList = [num**2 for num in range(0,100) if num % 2 !=0]
print(my_EvenFilterList)
# for filter odd even 
my_OddFilterList = [num**2 for num in range(0,100) if num % 2 ==0]
print(my_OddFilterList)