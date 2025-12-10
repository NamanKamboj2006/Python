A = input ("Enter Name: ")

print(A)
print(type(A))

# Why input is always string?

# Because Python does not know whether the user intends the input to be:
# a number
# text
# a decimal
# something else
# So it safely treats everything as text first.

# Convert input to integer:
age = int(input("Enter age: "))

# Convert input to float:
price = float(input("Enter price: "))


a = input("Enter a number: ")   # string
a = int(a)                      # converted to integer
