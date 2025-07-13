# How to changes in tuple (Note: Tuple are immutable)

t = (1, 2, 3)

# Step 1: Convert to list
temp_list = list(t)

# Step 2: Modify the list
temp_list.append(4)

# Step 3: Convert back to tuple
t = tuple(temp_list)

print(t)  # Output: (1, 2, 3, 4)
