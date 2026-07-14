#find the amount of capital letters in a string
def count_caps(word):
    count = 0
    for i in word:
        if i.isupper() == True:
            count = count + 1
    return count
word = "heLloHeLLo"
print(count_caps(word))

