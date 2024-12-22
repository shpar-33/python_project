# pure functions
def multiply_by3(li):
    new_list = []
    for item in li:
        new_list.append(item*3)
    return new_list
print(multiply_by3([1,2,3]))