
""" Difference between tuples & Lists :
Lists are mutable - items can be added, modified and deleted
Tuples are immutable - items cant be modified once added.
Usecase of Tuples : Data which need not be changed ever, ex : coordinates
representation : () """


coordinates = (10,20)
print(coordinates)
print(coordinates[0])
print(coordinates[1])
#print(coordinates(2))

#coordinates[1] = 23 #throws an error as tuples cant be modifed.
#print(coordinates)

#we can create a list of tuples

coordinates = [ (10,20), (30,40), (54,23)]
print(coordinates)
print(coordinates[1])
