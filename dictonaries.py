from collections import Counter
with open("textfile.txt") as f:
    words = f.read().split()
    common_words = Counter(words).most_common(5)
print(common_words)
