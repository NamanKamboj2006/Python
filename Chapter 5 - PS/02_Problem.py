# Write a program to input eight numbers from the user and display all the unique numbers (once).

x = set()

n1 = int(input("Enter Num 1: "))
x.add(n1)
n2 = int(input("Enter Num 2: "))
x.add(n2)
n3 = int(input("Enter Num 3: "))
x.add(n3)
n4 = int(input("Enter Num 4: "))
x.add(n4)
n5 = int(input("Enter Num 5: "))
x.add(n5)
n6 = int(input("Enter Num 6: "))
x.add(n6)
n7 = int(input("Enter Num 7: "))
x.add(n7)
n8 = int(input("Enter Num 8: "))
x.add(n8)

print("Unique numbers entered:", x)
