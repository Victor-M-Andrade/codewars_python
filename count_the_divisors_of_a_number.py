def divisors(n):
    divisors = 0
    for i in range(n):
        if n%(i+1) == 0:
            divisors += 1
    return divisors
