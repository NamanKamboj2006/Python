# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter The Number: "))

for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")