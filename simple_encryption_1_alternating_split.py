"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.

"""

def encrypt(text, n):
    odd = '' #impar
    even = '' #par
    result = text
    for i in range(n):
        for i in range(len(result)):
            if i == 0:
                even += result[i]
            else:
                if i % 2 == 0:
                    even += result[i]
                else:
                    odd += result[i]
        result = odd + even
        odd, even = '', ''

    return result


def decrypt(encrypted_text, n):
    aux, decry_one, decry_two = '', '', ''
    result = encrypted_text

    for i in range(n):
        mid = int(len(encrypted_text)/2)

        decry_one = result[0:mid]
        decry_two = result[mid:]

        for i in range(mid):
            aux += decry_two[i] + decry_one[i]
        
        if len(encrypted_text) % 2 != 0:
            aux += decry_two[mid]

        result = aux
        aux, decry_one, decry_two = '', '', ''
    
    return result




test = encrypt('012345', 2)
print(test)

test2 = decrypt('304152', 2)
print(test2)