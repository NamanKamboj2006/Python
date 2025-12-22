#  Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

mydict = {
    "namaste": "Hello",
    "madad": "Help",
    "billi": "Cat"
}

target = input("Enter the word you want to search: ").lower()

print(mydict[target])
# print(mydict.get(target))