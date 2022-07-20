def anagram_lst(lst):
    anagram = []
    for word1 in lst:
        for word2 in lst:
            if sorted(word1) == sorted(word2) and word1 != word2:
                anagram.append(word1)
    return anagram


print(anagram_lst(['dog','god','cat','act','tack','star','rat',
                    'rats']))


#comprehension #1
def anagrams(lst):
    anagrams_lst = []
    [anagrams_lst.append(word_1)
    for word_1 in lst
    for word_2 in lst
    if word_1 != word_2
    if sorted(word_1) == sorted(word_2)
    if word_1 not in anagrams_lst]

    return anagrams_lst

print(anagram_lst(['dog','god','cat','act','tack','star','rat',
                    'rats']))

#comprehension #2
def anagrams(lst):
    return list(set([ word_1
    for word_1 in lst
    for word_2 in lst
    if word_1 != word_2
    if sorted(word_1) == sorted(word_2) ]))


print(anagram_lst(['dog','god','cat','act','tack','star','rat',
                    'rats']))

#comprehension #3
def anagrams(lst):
    return [word
    for i, word in sorted(
        set([ (i, word_1)
        for i, word_1 in enumerate(lst)
        for word_2 in lst
        if word_1 != word_2
        if sorted(word_1) == sorted(word_2)
        ])
    )]

print(anagram_lst(['dog','god','cat','act','tack','star','rat',
                    'rats']))