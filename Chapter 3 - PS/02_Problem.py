# Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
Name = input("Enter Your Name: ")
Date = input("Enter Date: ")

letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)

print(letter)

