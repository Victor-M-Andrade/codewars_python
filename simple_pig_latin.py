"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""

def pig_it(text):

    split_sentence = text.split()

    pig_sentence = ' '

    for word in split_sentence:
        if word in '!.%&?':
            pig_sentence += word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence += pig_word + ' '

    return pig_sentence.strip(' ')


print(pig_it('This is my string'))
