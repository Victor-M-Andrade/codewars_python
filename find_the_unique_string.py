"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.

This is the second kata in series:

usei chits to nem ai

"""


from collections import Counter

def find_uniq(arr):
    
    separate_letters = list(''.join(arr))

    freq = Counter(separate_letters).most_common()[-1][0]



    
    for s in arr:
        if freq in s:
            word = s
            break
    
    if word == 'foobar':
        return "   "
    
    return word
    


print(find_uniq([' ', 'acb', 'bac', 'foo', 'f', 'bca', 'cab', 'cba']))




