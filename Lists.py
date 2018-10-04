""" Lists in Python
#Structure to store data values - organise and keep track of data
can add different types of values. ex : strings, numeric, boolean
representation : [] square brackets
"""

friends = ["Imran", "Badri", "Divya", "Lakshmi", "Ramya"]

print(friends)
print(friends[0])
#print(friends[10]) #Index out of range error
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[1:3])
print(friends[1:])
friends[1] = "Badrinath"
print(friends)