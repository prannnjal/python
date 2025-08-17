# list=["apple", "banana", "cherry", 1, 2, 3, "hi"]
# print(list[1])  # Accessing the first element of the list
# list[1] = "orange"  # Replacing "banana" with "orange"
# print(list[1])
# list.append("kiwi")  # Adding "kiwi" to the end of the list
# print(list)
# para=[111, 2, 3, 85, 90, 9, 45, 90, 100]
# print(para)  # Accessing the fourth element of the list
# para.sort()
# print(para)
# para.reverse()
# print(para)
# para.pop(0)  # Removing the element at index 2
# para.remove(90)
# print(para)
# print(type(para))  # Checking the type of the list
# practice
b = []
b1 = int(input("Enter a number: "))
b.append(b1)
b2 = int(input("Enter another number: "))
b.append(b2)
b3 = int(input("Enter one more number: "))
b.append(b3)
b4 = int(input("Enter a final number: "))   
b.append(b4)

print(b)  # Printing the list of numbers
b.sort()  # Sorting the list of numbers
print(b)  # Printing the sorted list of numbers
print(sum(b))  # Printing the sum of the numbers in the list