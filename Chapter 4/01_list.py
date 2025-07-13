list = ["Apple", "Mango", "Banana", 10, True] # str are immutable [possible in list]

print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print("---- Update List ----")
list[0] = "Japan"
list[3] = "Hi"
list[4] = False
print(list)
print("=== Slicing ===")
print(list[0:4])
print(list[0:])