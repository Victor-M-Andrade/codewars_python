
def tribonacci(signature, n):
    tab = signature

    for i in range(n):
        tab.append(-1)
    
    
    def tri(n):
        if tab[n] == -1:
            tab[n] = tri(n-1) + tri(n-2) + tri(n-3)
        return tab[n]
    
    tri(n)
    print(tab[:10])

tribonacci([1, 1, 1], 10)