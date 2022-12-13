x = 4183059834009
i = 0
total = 0
while total < x:
    total += (i+1)**3
    i += 1

if total == x:
    print('Verdadeiro')
else:
    print('Falso')


def find_nb(m):
    i = 0
    total = [0]
    while sum(total) < m:
        total.append((i+1)**3)
        i += 1
    if sum(total) == m:
        return len(total)-1
    else:
        return -1