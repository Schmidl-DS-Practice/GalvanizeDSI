def num_in_word(s):

    if s == '':
        return ''
    ordered_s = []
    for ele in s.split():
        for char in ele:
            if char.isdigit():
                ordered_s.append((char,ele))

    sentence = ''
    for i in sorted(ordered_s):
        sentence += i[1] + ' '

    return sentence.strip()

print(num_in_word('is2 Thi1s T4est 3a'))
print(num_in_word('4of Fo1r pe6ople g3ood th5e the2'))

def order(sentence):
    return " ".join(
        [ word
        for num, word in sorted(
            [ (char, word)
            for word in sentence.split(" ")
            for char in word
            if char.isdigit()
            ] )
        ])

print(order('is2 Thi1s T4est 3a'))
print(order('4of Fo1r pe6ople g3ood th5e the2'))
