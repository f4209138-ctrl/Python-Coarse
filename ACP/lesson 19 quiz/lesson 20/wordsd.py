def match_words(words):
    ctr = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print(lst)
    return ctr


sample_words = ["abc", "xyz", "aba", "1221", "a"]
count = match_words(sample_words)

print(count)