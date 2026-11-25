# Problem: Write a function compress(text) that replaces each run 
# of repeated characters with the character followed by the run's length. 
# You can assume the input contains no digits.

def compress(text: str) -> str:
    def cut_text(text : str, count : int, cut_end : int) -> str:
        cut_start : int = cut_end + 1 - count
        new_text : str = text[0:cut_start] + f"{count}" + text[cut_end:len(text)]
        return new_text

    def move_iterator(i : int, count : int) -> int:
        chars_added = len(f"{count}")
        chars_removed = count - 1
        return i + chars_added - chars_removed
    
    if len(text) == 0: return text

    i : int = 1
    repeats : int = 1
    while i < len(text):
        if text[i] == text[i-1]:
            repeats += 1
        else:
            text = cut_text(text, repeats, i)
            i  = move_iterator(i, repeats)
            repeats = 1
        i += 1
    text = cut_text(text, repeats, i)
    return text

def decompress(text: str) -> str:
    def determine_current_letter():
        nonlocal current_letter
        nonlocal i
        nonlocal repeats
        if not text[i].isdigit():
            current_letter = text[i]
            i += 1
            repeats = 0
    
    def determine_repeats():
        nonlocal repeats
        nonlocal i
        while i < len(text) and text[i].isdigit():
            repeats = (repeats * 10) + int(text[i])
            i += 1
    
    i : int = 0
    new_text : str = ""
    repeats : int = 0
    current_letter : str = '' # Why does doing "": chr" not work?
    while i < len(text):
        determine_current_letter()
        determine_repeats()
        new_text = new_text + current_letter * repeats
    return new_text

print("Spec examples")
print(compress("aaabbc"), "expected a3b2c1")
print(compress("abc"), "expected a1b1c1")
print(compress(""), "expected (empty string)")
print(compress("aaaaaaaaaaaa"), "expected a12")
print(compress("aabbaa"), "expected a2b2a2")
print(compress("zzzz"), "expected z4")

print("Edge cases")
print(compress("a"), "expected a1")
print(compress("aA"), "expected a1A1")
print(compress("aaAA"), "expected a2A2")
print(compress("  !!"), "expected  2!2")   # two spaces, then two exclamation marks
print(compress("abababab"), "expected a1b1a1b1a1b1a1b1")
print(compress("xxxxxxxxxxy"), "expected x10y1")

print("Bonus: decompress")
print(decompress("a3b2c1"), "expected aaabbc")
print(decompress(""), "expected (empty string)")
print(decompress("a12"), "expected aaaaaaaaaaaa")
print(decompress(" 2!2"), "expected   !!")
print(decompress(compress("xxxxxxxxxxy")), "expected xxxxxxxxxxy")