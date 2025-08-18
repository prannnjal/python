a={"name": "John", "age": 30, "city": "New York"}
print(a["age"])  # Printing the dictionary
print(a.items())  # Printing the items in the dictionary
print(a.keys())  # Printing the keys in the dictionary
a.update({"age": 31, "height": 175})  # Updating the age and adding height to the dictionary
print(a["age"])  # Printing the updated age
print(a)  # Printing the added height
print(a.get("namee"))  # Using get to retrieve the name
b=dict.copy(a)  # Copying the dictionary a to b
print(b)  # Printing the copied dictionary
# a.clear()  # Clearing the dictionary a
# print(a)  # Printing the cleared dictionary
a.pop("city")  # Removing the city from the dictionary
print(a)  # Printing the dictionary after removing city
a.popitem()  # Removing the last inserted item from the dictionary
print(a)  # Printing the dictionary after popping the last item