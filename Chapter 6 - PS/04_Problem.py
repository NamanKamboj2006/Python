# Write a program to find whether a given username contains less than 10 characters or not.

name = input("Enter Your Name: ")

if(len(name) < 10):
    print(f"You {name} length is less than 10")
else:
    print(f"You {name} length is greator than 10")
