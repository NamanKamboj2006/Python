# Can we have a set with 18 (int) and '18' (str) as a value in it?

x = set()

n1 = int(input("Enter Num 1: "))
x.add(n1)
n2 = input("Enter String 1: ")
x.add(n2)

print(x)