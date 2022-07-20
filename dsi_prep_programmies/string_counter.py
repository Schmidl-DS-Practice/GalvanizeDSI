def new_st_counter(s):
    dic = {'num_char': 0, 'upper_case': 0, 'lower_case': 0, 'capital_words': 0, 
           'unique_words_start_vowel': 0, 'avg_word_leng': 0}
    count_upper = 0
    count_lower = 0
    cap_words = []
    unique_words_vowel = []
    
    for k in dic.keys():
        for let in s:
            dic['num_char'] += 1
            if let.isupper():
                count_upper += 1
                dic['upper_case'] = count_upper
            elif let.islower():
                count_lower += 1
                dic['lower_case'] = count_lower
        num = []
        for word in s.split():
            if word[0].isupper():
                cap_words.append(word)
                dic['capital_words'] = cap_words
            elif word not in unique_words_vowel:
                vowel_lst = ['a','e','i','o','u']
                if word[0] in vowel_lst:
                    unique_words_vowel.append(word)
                    dic['unique_words_start_vowel'] = unique_words_vowel
            
            num.append(len(word))
            average = sum(num)/len(s.split())
            dic['avg_word_leng'] = average
    return dic
print(new_st_counter('''Just a small-town girl Livin\' in a lonely world! She took the midnight train goin\' anywhere.
Just a city boy Born and raised in South Detroit. He took the midnight train goin\' anywhere?
A singer in a smoky room. The smell of wine and cheap perfume? For a smile they can share the night
It goes on and on, and on, and on. Strangers waiting Up and down the boulevard. 
Their shadows searching in the night! Streetlights people Livin\' just to find emotion! 
Hidin\' somewhere in the night!'''))
# str1 = 
# str2 = '''It\'s a beautiful day! Sky falls, you feel like It\'s a beautiful day
# Don\'t let it get away You\'re on the road, but you\'ve got no destination
# You\'re in the mud, in the maze of her imagination You love this town even if that doesn\'t
# ring true You\'ve been all over, and it\'s been all over you'''
