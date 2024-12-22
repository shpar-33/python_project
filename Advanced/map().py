#map, filter, zip, and reduce
# map(action, data)
my_list = [1,2,3,4,5]
def multiplyby3(item):
    return item*3

print(list(map(multiplyby3,my_list)))
#print(my_list)