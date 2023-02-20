import wikipedia
s = input("")
res = wikipedia.summary(s,sentences = 2)
print(res)