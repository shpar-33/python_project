# 1
# def generator_function(num):
#     for i in range(num):
#         yield i

# for item in generator_function(1000):
#     print(item)

#2
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             next(iterator) 
#         except StopIteration:
#             break 
# special_for([1,2,3])

#3
# class MyGen():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     def __iter__(self):
#         return self


# gen = MyGen(0,100)

# for i in gen: 
#     print(i)


