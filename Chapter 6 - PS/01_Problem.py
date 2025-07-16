# Write a program to find the greatest of four numbers entered by the user

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))
d = int(input("Enter 4th Number: "))

if(a>b and a>c and a>d):
    print(f"{a} is greater")
elif(b>a and b>c and b>d):
    print(f"{b} is greater")
elif(c>a and c>b and c>d):
    print(f"{c} is greater")
else:
    print(f"{d} is greater")

