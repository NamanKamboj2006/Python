# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

for greet in l:
    if(greet.title().startswith("S")):
        print(f"Greeting {greet}")
