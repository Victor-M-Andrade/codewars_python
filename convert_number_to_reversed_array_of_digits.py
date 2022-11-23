"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number
 within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]

"""

def digitize(n):
    n_list = [int(x) for x in str(n)]
    invert = []
    for i in range(len(n_list)):
        invert.append(n_list[-(i+1)])
    return invert


print(digitize(35231))