
teste = '()'

teste2 = list(teste)
print(teste2)

open = 0

close = 0

if teste2[1] == ')':
    resultado = False

else:
    for i in range(len(teste2)):
        if teste2[i] == '(':
            open = 1
        if teste2[i] == ')':
            close += 1
        if close > open:
            resultado = False
    
    if open == close:
        resultado = True
    else:
        resultado = False


print(open)