my_list = [1,2,3]
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))

# my_list = [1,2,3,4,5,6,7,8,9,10]
# def only_even(item):
#     return item % 2 == 0

# print(list(filter(only_even, my_list)))
