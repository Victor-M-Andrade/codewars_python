"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

"""

def square_digits(num):
    num = list(str(num))
    valors = []
    for i in range(len(num)):
        valors.append(str(int(num[i])**2))
    return int(''.join(valors))


print(square_digits(9119))