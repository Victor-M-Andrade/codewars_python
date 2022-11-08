#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#Na minha opiniao o exercicio esta errado , mas tudo bem, ele passou no teste

def solution(string, ending):
    
    string_new = list(string)
    ending_new = list(ending)

    if ending_new[:] == string_new[-len(ending_new):]:
        return True
    elif ending_new == []:
        return True
    else:
        return False


x = solution('abcde', '')
print(x)