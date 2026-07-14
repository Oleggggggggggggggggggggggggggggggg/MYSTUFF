vowels = ["a", "o", "e", "i", "u"]
word = "Hello"
def vowel_check(word):
    sum = 0
    word = word.lower()
    for i in range(0, len(word)):
        for vowel in vowels:
            if word[i] == vowel:
                sum = sum + 1
    return sum
print(vowel_check("Infinity"))

