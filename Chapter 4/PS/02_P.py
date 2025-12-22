# Write a program to input 4 numbers from the user and display all the unique
# numbers (once)

myset = set()

# myset.add(int(input("Enter Number 1: ")))
n = int(input("Enter Number 1: "))
myset.add(n)
n = int(input("Enter Number 2: "))
myset.add(n)
n = int(input("Enter Number 3: "))
myset.add(n)
n = int(input("Enter Number 4: "))
myset.add(n)

print(myset)