# Write a program to find whether a given number is prime or not.

num = int(input("Enter A Number: "))

if num<2:
    print("Pls, Enter no greator than or equal to 2")
    exit()
elif num==2:
    print(f"{num} is a prime no")
    exit()
elif num % 2 == 0:
    print(f"{num} is not a prime number")
    exit()

for i in range(3, ((num)//2)+1, 2):
    if(num%i == 0):
        print(f"{num} is not a prime no")
        break
else:
    print(f"{num} is a prime no") 