str = input()
counts = dict()
words = str.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for key in counts.keys():
    print(key, counts[key])
