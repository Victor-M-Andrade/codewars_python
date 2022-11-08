#You will be given a number and you will need to return it as a string in Expanded Form. For example:

#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'

#reference = https://www.mathsisfun.com/definitions/expanded-notation.html




def expanded_form(num):
    num_list = list(str(num))

    expanded_form = []

    for i in range(len(num_list)):
        expanded_form.append(int(num_list[i])*(10**(len(num_list)-(i+1))))

    for i in range(len(expanded_form)):
        if 0 in expanded_form:
            expanded_form.remove(0)

    string = ' + '.join(str(x) for x in expanded_form)

    return string



teste = expanded_form(42)

print(teste)