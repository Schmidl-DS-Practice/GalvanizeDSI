def new_st_counter(s):
  '''
  a function that creates a dictionary that contains a
  list of words in the string based on their frequency
  in ascending order, a list of the top ten most
  frequently used words in descending order and a
  dictionary of counts of alpha characters

  Parameters:
  s: string
    a string
  
  Returns:
    a dictionary with key value pairs based on the
    prompt
  '''
  dic_of_things = {'word_in_string': [], 'top_ten': [],
                   'alpha_char_count': {}}
  for char in s:
    if char.isalpha() and char in dic_of_things['alpha_char_count']:
      dic_of_things['alpha_char_count'][char] += 1
    elif char.isalpha() and char not in dic_of_things['alpha_char_count']:
      dic_of_things['alpha_char_count'][char] = 1

  punc = [',','.','!','?']
  for p in punc:
    replace_me = s.replace(p, ' ')
  
  split_me = replace_me.split()
  
  word_counts = {}
  for wor in split_me:
    if wor not in word_counts:
      word_counts[wor] = 1
    else:
       word_counts[wor] += 1
  tup_l = [(v, k) for k, v in word_counts.items()]
  tup_l_sorted = sorted(tup_l)

  dic_of_things['word_in_string'] = [tup[1] for tup in tup_l_sorted]
  
  dic_of_things['top_ten'] = dic_of_things['word_in_string'][:-11:-1]

  

  
  return dic_of_things


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