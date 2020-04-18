def word(s):
    counts={}
    for char in s:
        counts[char]=s.count(char)
    return counts 

print(word("hello"))