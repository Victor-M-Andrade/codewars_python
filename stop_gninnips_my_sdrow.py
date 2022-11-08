#Write a function that takes in a string of one or more words, 
# and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    sentence_list = sentence.split()

    for i in range(len(sentence_list)):
        if len(sentence_list[i]) >= 5:
            change = sentence_list[i]
            change = change[::-1]
            sentence_list[i] = change
    
    return ' '.join(sentence_list)


#print(x[::-1])

teste = spin_words('Hey fellow warriors')

print(teste)