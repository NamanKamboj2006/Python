# Functions can return values using the return statement:
def func1(x, y):
  return x + y

result = func1(5, 3)
print(result)

# A function that returns a list:
def func2():
  return ["apple", "banana", "cherry"]

fruits = func2()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# A function that returns a tuple:
def func3():
  return (10, 20)

x, y = func3()
print("x:", x)
print("y:", y)

