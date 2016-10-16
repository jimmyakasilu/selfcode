n = int(raw_input())
words = {}
for i in xrange(n):
    word = raw_input()
    listy = set(words.keys())
    if word in listy:
        words[word] += 1
    else:
        words[word] = 1
print words
