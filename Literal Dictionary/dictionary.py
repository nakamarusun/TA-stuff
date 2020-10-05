import string

english_dictionary = {}

with open("words.txt", "r", encoding="utf-8") as file:
    for word in file:
        first_letter = word[0].upper()
        if (first_letter in string.ascii_uppercase):
            if first_letter not in english_dictionary:
                english_dictionary[first_letter] = [word.strip().capitalize()]
            else:
                english_dictionary[first_letter].append(word.strip().capitalize())

print(len(english_dictionary))
print(english_dictionary["Q"][30])