# arguments inside function 
# variables 
# higher order function HOC
# function wraps another functions 

def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('helloooo')

@my_decorator
def bye():
    print('see ya')
    
hello()
bye()

# hello2 = my_decorator(hello)
# hello2()
# my_decorator(hello)()

