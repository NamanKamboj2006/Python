# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

hindi_to_english = {
    "pani": "water",
    "khana": "food",
    "namaste": "hello",
    "dhanyavaad": "thank you",
    "pyaar": "love",
    "ghar": "home",
    "school": "school",
    "ladka": "boy",
    "ladki": "girl",
    "kitaab": "book",
    "billi": "cat",
    "kutta": "dog",
    "suraj": "sun",
    "chaand": "moon",
    "aakaash": "sky",
    "ped": "tree",
    "phal": "fruit",
    "sabzi": "vegetable",
    "kaam": "work",
    "accha": "good",
}


word = input("Enter A Hindi Word: ").lower()



print(hindi_to_english.get(word))