# A spam comment is defined as a text containing following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this". Write a program
# to detect these spams.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Enter Your Comment: ").lower()
if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("This Text is not allowed")
else:
    print("Not Spam")