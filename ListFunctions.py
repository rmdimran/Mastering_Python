
lucky_numbers = [12,15,23,30,45,64,10]
friends = ["Imran", "Divya", "Badri", " Lakshmi", "Ravi", "Chinky"]

print(friends)
print(lucky_numbers)

friends.extend(lucky_numbers) #add two list together
print(friends)

friends.append("Datta") #add items to the list always at the end
print(friends)

friends.insert(4, "Rahul") #insert elements at a particular index
print(friends)

friends.remove("Datta") #remove particular value from the list
print(friends)

friends.clear() #reset the list
print(friends)

lucky_numbers = [12,15,23,30,45,64,10]
friends = ["Imran", "Divya", "Badri", " Lakshmi", "Ravi", "Chinky", "Imran"]

print(friends.pop()) #removes the last element of the list
print(friends.index("Ravi")) #to check if the value exists
#print(friends.index("ramu")) #element not in the list error

friends = ["Imran", "Divya", "Badri", "Lakshmi", "Ravi", "Chinky", "Imran"]
print(friends.count("Imran"))

friends.sort() #sort the list in alphabetical order
lucky_numbers.sort() #sort in ascending order
print(friends)
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)


