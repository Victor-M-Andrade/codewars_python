#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.


def find_short(s):
    s = s.split()

    qtd_letters = []

    for i in range(len(s)):
        qtd_letters.append(len(s[i]))
    
    qtd_letters = sorted(qtd_letters, key=int, reverse=True)


    return qtd_letters[-1]


teste = find_short('lets talk about javascript the best language')

print(teste)