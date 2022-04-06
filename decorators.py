# Reference Link for better understanding:
# https://www.datacamp.com/community/tutorials/decorators-python

#Function inside functions & How to Return function ==>>
print("=======Part 1:->\n")


def hello(name='sdp'):

    print('Inside hello()...!')

    def welcome():
        return "Inside Welcome() ...!"

    def greet():
        return "Inside greet()...!"

    if name == 'sdp':
        # look at syantax here carefully... not welcome(), its just welcome
        # If i return welcome(), it means i return a value returned by welcome() function...
        return welcome
    else:
        return greet

# hello() will return a function, so basically, it means SYNTAX: x = welcome and not x = welcome()
x = hello("boy")
print(x())
#OUTPUT: Inside hello()...!  Inside greet()...!

y = hello() #here default argument as 'sdp' is passed...!
print(y())
# OUTPUT: Inside hello()...! Inside Welcome() ...!




####################################################################################################################
# Function as Argument ==>
print('======Part 2:\n')
def hello():
    return "Hi Jose ...!"


def other(func):
    print("Hello...!")
    # Now we can play with func() this function.....
    print(func())

#let's pass function as parameter:
other(hello)

#If we pass like below, it means we are passing value returned by hello():
# other(hello())






#####################################################################################################################
#Decorator ==>>>
print('========Part 3:\n')

def new_decorator(func):

    def wrap_func():
        print("code here before executing func...!")
        func()
        print("func() has been called...!")

    #return function
    return wrap_func


# def func_need_decorator():
#     print("This function is in need of decorator ...!")
# #lets pass function as Argument here:->
# func_need_decorator = new_decorator(func_need_decorator)

# All above can be written as:
@new_decorator
def func_need_decorator():
    print("This function is in need of decorator ...!")

func_need_decorator()
