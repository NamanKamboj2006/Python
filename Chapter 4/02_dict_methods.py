# Create a dictionary
d = {
    "name": "Naman",
    "age": 20,
    "course": "Python"
}

print("Original dictionary:", d)

# get()
print("Name:", d.get("name"))

# keys()
print("Keys:", d.keys())

# values()
print("Values:", d.values())

# items()
print("Items:", d.items())

# copy()
d_copy = d.copy()
print("Copied dictionary:", d_copy)

# setdefault()
d.setdefault("city", "Delhi")
print("After setdefault:", d)

# update()
d.update({"age": 21, "college": "ABC College"})
print("After update:", d)

# pop()
d.pop("course")
print("After pop:", d)

# popitem()
d.popitem()
print("After popitem:", d)

# fromkeys()
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Dictionary from fromkeys():", new_dict)

# clear()
d.clear()
print("After clear:", d)
