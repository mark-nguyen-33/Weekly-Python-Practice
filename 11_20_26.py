# Problem: Write a function is_balanced(text) that returns True if every opening bracket in the string 
# has a matching closing bracket in the correct order, and False otherwise. 
# The bracket types are (), [], and {}. Ignore all other characters.

def is_balanced(text : str) -> bool:
    delimiters = []
    openers = "({["
    closers = ")}]"
    for i in range(len(text)):
        if text[i] in openers:
            delimiters.append(text[i])
        elif text[i] in closers and not closer_check(delimiters, text[i]):
            return False
    if len(delimiters) != 0:
        return False
    return True

def closer_check(stack : list[str], closer : str) -> bool:
    openers = "({["
    closers = ")}]"
    if len(stack) == 0 : return False
    if openers.index(stack.pop()) != closers.index(closer): return False
    return True

print("Spec examples")
print(is_balanced("()"), "expected True")
print(is_balanced("([]{})"), "expected True")
print(is_balanced("(]"), "expected False")
print(is_balanced("([)]"), "expected False")
print(is_balanced("(("), "expected False")
print(is_balanced(")("), "expected False")
print(is_balanced("a(b)c[d]"), "expected True")
print(is_balanced(""), "expected True")

print("Edge cases")
print(is_balanced("("), "expected False")
print(is_balanced(")"), "expected False")
print(is_balanced("{[()()]}"), "expected True")
print(is_balanced("{[(])}"), "expected False")
print(is_balanced("()()()"), "expected True")
print(is_balanced("(()"), "expected False")
print(is_balanced("())"), "expected False")
print(is_balanced("hello world"), "expected True")
print(is_balanced("[{()}](){}"), "expected True")