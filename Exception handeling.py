try:
    # we put the portion of the code here where error can take place
    div = 10/2
except ZeroDivisionError:
    # this portion executed only if there are any error in try block
    print('Looks like you are dividing by zero!')
else:
    # This block will execute if there is no exception raised in the try block
    print('Division went well')
    print('Result is: ', div)
finally:
    # This block will execute no matter what
    print('Finally block executed, whatever happens')



print("\n")


try:
    div = 10@2
except TypeError:
    print('You have Typed Wrong Symbol!')
else:
    print('Result is: ', div)
