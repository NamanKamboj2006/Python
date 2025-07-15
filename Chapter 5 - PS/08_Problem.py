# If languages of two friends are same; what will happen to the program in problem 6?

fav_lang = {} # Empty

name1 = input("Enter name of friend 1: ")
lang1 = input("Enter their favorite language: ")
fav_lang.update({name1:lang1})
# fav_lang[name1] = lang1

name2 = input("Enter name of friend 2: ")
lang2 = input("Enter their favorite language: ")
fav_lang.update({name2:lang2})
# fav_lang[name2] = lang2

name3 = input("Enter name of friend 3: ")
lang3 = input("Enter their favorite language: ")
fav_lang.update({name3:lang3})
# fav_lang[name3] = lang3

name4 = input("Enter name of friend 4: ")
lang4 = input("Enter their favorite language: ")
fav_lang.update({name4:lang4})
# fav_lang[name4] = lang4

print("\nFavorite languages dictionary:")
print(fav_lang)