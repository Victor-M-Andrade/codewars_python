"""
Crie um fluxo infinito de números primos - um pouco como IntStream.of(2, 3, 5, 7, 11, 13, 17),
 mas infinito. O fluxo deve ser capaz de produzir um milhão de primos em poucos segundos.

"""

class Primes:
    @staticmethod
    def stream():
        from math import ceil
        limit = 15490000
        primes = [True]*limit
        for base in range(2, int(limit**0.5 + 1)):
            if primes[base]:
                primes[base*2:limit:base] = [False]*(ceil(limit / base) - 2)
        primes[0] = primes[1] = False
        p = (num for num, is_prime in enumerate(primes) if is_prime)
        for i in p:
            yield i