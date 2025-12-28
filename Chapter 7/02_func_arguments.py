def my_function(name):
  print("Good Morning", name)

my_function("Naman")
my_function("Mukul")
my_function("Manan")

def my_function(name1, name2, name3):
  print(f"Good Morning, {name1}, {name2} and {name3}")

my_function("Naman", "Mukul", "Manan")

# Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Mouser")

# Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
