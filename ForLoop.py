#Example : 1

for letter in "Imran":
    print(letter)

#Example : 2

friends = [ "Imran", "ravi", "Ram"]
for friend in friends:
    print(friend)

#Example : 3

friends = [ "Imran", "ravi", "Ram"]
for index in range(len(friends)):
    print(friends[index])

# Example : 4
for num in range(20):
    print(num)

# Example : 5
for num in range(10,20):
    print(num)

# Example : 6
for index in range(5):
    if index == 0:
        print("You are in First Iteration.")
    else:
        print("Not in first iteration.")