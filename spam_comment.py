# p1= "nice"
# p2= "good"
# p3= "excellent"
# p4= "outstanding"

# message = input("Enter your comment: ")

# if p1 in message or p2 in message or p3 in message or p4 in message:
#     print("This is a spam comment")

l1 = ["nice", "good", "excellent", "outstanding"]
message = input("Enter your comment: ")

if any(x in message for x in l1):
    print("your name is present ")
else:
    print("your name is not present ")
