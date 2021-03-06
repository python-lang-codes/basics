# HEAD
# Python Functions - No Return, Single Return, Multiple returns
# DESCRIPTION
# Describes returning values from functions
#
# Can have Single return value from function
# 'return' value, when is a single return value
#       keeps the type in return statement
# Can return multiple values from a function
# 'return' values, when multiple return values,
#       gets coverted to the type of tuple
# Python has First-class functions - https://en.wikipedia.org/wiki/First-class_function
#           It treats functions as first-class citizens, means the language supports passing
#           functions as arguments to other functions, returning them as the
#           values from other functions, and assigning them to variables or
#           storing them in data structures.
# 
# RESOURCES
# 

# Return values can be captured in a variable
#       during invocation (Single or Multiple return values)
# Values can be destructured and assigned
#       to multiple variables (Multiple return values)
# The return values are of specific types as returned
#       and not a tuple in this case
# The number of items in the destructuring have to be
#       the same as variables used for assignation

# A function with no return value returns a None value
# A function with a return statement and no value in return
#       returns a None value
# A function can return one return value
# A function can return multiple return values - type will be tuple
# https://stackoverflow.com/questions/39345995/how-does-python-return-multiple-values-from-a-function
# A function can pack multiple return values into a
#       different type but construct them into a different 
#       type like list or diction or set


# Declaring a function with no return
def no_return():
    print("Testing no return statement")


# Following prints None
noreturn = no_return()
print(noreturn)


# Declaring a function with blank return
def blank_return():
    print("Testing return statement with no value")
    return


# Following prints None
blankreturn = blank_return()
print(blankreturn)


# Declaring a function with None as return
def none_return():
    print("Testing return statement with no value")
    return None


# Following prints None
nonereturn = none_return()
print(nonereturn)


# Return values can be captured in a variable
#       during invocation (Single or Multiple return values)
# Values can be destructured and assigned
#       to multiple variables (Multiple return values)
#       The return values are of specific types as returned
#       and not a tuple in this case of destructuring.
#       The number of items in the destructuring have to be
#       the same as variables used for assignation.


# Declaring a function with single return
def hello(name):
    print('Howdy! ' + name)
    return name


# Following prints value of 'name' variable
singleret = hello('Testing Single Return')
print(singleret)


# Declaring a function with multiple return values
def helloMultiple(name):
    print('Howdy! ' + name)
    # Following two return statements are equal
    # Explicit
    # return ('name', name)
    # Implicit
    return 'name', name


# Capture multiple returns as a tuple
mul = helloMultiple('Testing Multiple returns')
print(mul)


# Return tuple (default) with multiple items from function
def myfunReturnTupleImplicit():
    return 1, 2, 3
mul = myfunReturnTupleImplicit()
print(mul)


# Return tuple with multiple items from function
def myfunReturnTupleExplicit():
    return (1, 2, 3)
mul = myfunReturnTupleImplicit()
print(mul)


# Return set with multiple items from function
def myfunReturnSet():
    return {1, 2, 3}
mul = myfunReturnSet()
print(mul)


# Return dict with multiple items from function
def myfuncReturnDiction():
    return {0: 1, 1: 2, 2: 3}
mul = myfuncReturnDiction()
print(mul)


# Return list with multiple items from function
def myfunReturnList():
    return [1, 2, 3]
mul = myfunReturnList()
print(mul)


# Single line functions can also be defined
# It may act as a replacement for anonymous lamda functions
#       where you need named reference or 
#       reuse of function definitions and also return multiple returns
def func(x): return "some value", x
mul = func(1)
print(mul)

