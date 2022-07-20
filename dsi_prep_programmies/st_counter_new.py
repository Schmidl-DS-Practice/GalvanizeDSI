
import re
def new_st_counter(s):
    '''
    a function that creates a dictionary that the non-alpha
    characters and their frequencies, the number of sentences, a
    list of contractions, an average lenth of sentence in words and
    an average length of sentence in characters

    Parameters:
    s: string
        a string
    
    Returns:
    a dictionary with key value pairs based on the prompt
    '''
    dic = {'non_alpha_dictionary': {}, 'num_sentences': 0, 'contract_words': [],
           'avg_len_sent_words': 0, 'avg_len_sent_in_char': 0}
    non_alpha_chars = {}
    num_words = 0
    split_me = s.replace(',', '!').replace('?','!').split('!')
    num_char = []
    contract_list = []
    for sent in split_me:
        dic['num_sentences'] += 1
        num_char.append(len(sent))
        dic['avg_len_sent_in_char'] = sum(num_char) / len(split_me)
        count_spaces = sent.count(' ')
        num_words += count_spaces
        dic['avg_len_sent_words'] = num_words / len(split_me)
        for word in sent.split(' '):
            if "'" in word:
                contract_list.append(word)
                dic['contract_words'] = contract_list  
    for char in s:
        if char.isalpha() == False:
            count_chars = s.count(char)
            non_alpha_chars[char] = count_chars
            dic['non_alpha_dictionary'] = non_alpha_chars
    return dic

print(new_st_counter('''Just a small-town girl Livin\' in a lonely
world! She took the midnight train goin\' anywhere. Just a city boy
Born and raised in South Detroit. He took the midnight train goin\'
anywhere? A singer in a smoky room. The smell of wine and cheap
perfume? For a smile they can share the night It goes on and on,
and on, and on. Strangers waiting Up and down the boulevard. Their
shadows searching in the night! Streetlights people Livin\' just to
find emotion! Hidin\' somewhere in the night!'''))
print(new_st_counter('''It\'s a beautiful day! Sky falls, you feel
like It\'s a beautiful day. Don\'t let it get away! You\'re on the
road, but you\'ve got no destination? You\'re in the mud, in the
maze of her imagination! You love this town even if that doesn\'t
ring true. You\'ve been all over, and it\'s been all over you.'''))
