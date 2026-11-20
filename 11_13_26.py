# Problem: Write a function is_palindrome(text) that returns True 
# if the string reads the same forwards and backwards, and False 
# otherwise. It should ignore case, spaces, and punctuation.

def is_palindrome(text: str):
    letters = ""
    for letter in text.upper(): 
        if letter.isalpha() or letter.isdigit(): 
            letters += letter
    length = len(letters)
    for i in range(0, length//2):
        beginning_letter = letters[i]
        ending_letter = letters[length-1-i]
        if (beginning_letter != ending_letter):
            return False
    return True

print(f"Pip: {is_palindrome("Pip")}")
print(f"Pielo: {is_palindrome(" Pie lo ")}")
print(f"Abrba: {is_palindrome("Abrba")}")
print(f"A man, a plan, a canal: Panama: {is_palindrome("A man, a plan, a canal: Panama")}")
