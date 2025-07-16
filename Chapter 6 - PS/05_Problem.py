# Write a program which finds out whether a given name is present in a list or not.

NameList = ["naman", "manan", "mukul", "nitin", "navdeep"]

name = input("Enter Your Name: ").lower()

if(name in NameList):
    print(f"Your name: {name} is present in list")
else:
    print("Your name is not present in list")
