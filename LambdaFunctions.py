# Lambda functions : Also known as Functions without names - Anonymous functions

# General Functions
def square ( num ):
    return num * num


print ( square ( 20 ) )

# using lambda functions
# Example : 1
square = lambda num: num * num
print ( square ( 25 ) )

# Example : 2
add = lambda a, b: a + b
print ( add ( 200, -3 ) )
