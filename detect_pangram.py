"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
 the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

def is_pangram(s):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    list_s = list(s.lower())
    aux = []
    for i in range(len(s)):
        if list_s[i] in alphabet:
            aux.append(list_s[i])
    aux = sorted(set(aux), key=str, reverse=False)

    if aux == alphabet:
        return True
    else:
        return False


print(is_pangram('Cwm fjord bank glyphs vext quiz'))
