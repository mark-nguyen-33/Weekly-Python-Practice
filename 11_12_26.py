def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_dictionary = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for letter in word:
        if letter in vowels:
            vowel_dictionary[letter.lower()] = vowel_dictionary.get(letter.lower(), 0) + 1
    return vowel_dictionary


print(f"Hello: {count_vowels('Hello')}.")
print(f"PYTHON: {count_vowels('PYTHON')}.")
print(f"rhythm: {count_vowels('rhythm')}.")
print(f"Education: {count_vowels('Education')}.")