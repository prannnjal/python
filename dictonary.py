# a={"name": "John", "age": 30, "city": "New York"}
# print(a["age"])  # Printing the dictionary
# print(a.items())  # Printing the items in the dictionary
# print(a.keys())  # Printing the keys in the dictionary
# a.update({"age": 31, "height": 175})  # Updating the age and adding height to the dictionary
# print(a["age"])  # Printing the updated age
# print(a)  # Printing the added height
# print(a.get("namee"))  # Using get to retrieve the name
# b=dict.copy(a)  # Copying the dictionary a to b
# print(b)  # Printing the copied dictionary
# a.clear()  # Clearing the dictionary a
# print(a)  # Printing the cleared dictionary
# a.pop("city")  # Removing the city from the dictionary
# print(a)  # Printing the dictionary after removing city
# a.popitem()  # Removing the last inserted item from the dictionary
# print(len(a))  # Printing the dictionary after popping the last item

# Practice
# a={"naam": "name", "umar": "age","kaam": "work"}
# c=input("Enter the key to get the value: ")
# print(a.get(c, "Key not fo
# 
# und"))  # Using get to retrieve the value

a = {}
pairs = input("Enter the key-value pairs (key:value) separated by space: ").split(" ")
for pair in pairs:
    if ":" in pair:
        key, value = pair.split(":", 1)
        a[key] = value
print(a)  # Printing the dictionary with the key-value pairs
c = input("Enter the key to get the value: ")
print(a.get(c, "Key not found"))  # Using get to retrieve the value for the given key