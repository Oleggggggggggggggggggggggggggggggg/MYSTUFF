a = "hello cat"
thing = input()
def censor_cat(string, word):
    string = string.replace(word, "*"*len(word))
    return string

print(censor_cat(a, "cat"))
