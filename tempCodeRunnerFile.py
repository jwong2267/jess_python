WORD = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
word = []

for char in WORD:
    word.append(char)

# Code here

for i, letter in enumerate(word):
    i = 2
    while i <= len(word):
        word[i] = 0
        i +=3
print(word)