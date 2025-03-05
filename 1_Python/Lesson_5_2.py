word = input("Введите слово: ")

vowels = "aeiou"

vowels_count = (word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u"))

consonants_count = len(word) - vowels_count

if ("a" in word and "e" in word and "i" in word and "o" in word and "u" in word):
    print(f"Гласных: {vowels_count}, Согласных: {consonants_count}")
else: 
    print("False")