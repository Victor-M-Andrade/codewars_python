"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

"""

def abbrev_name(name:str):
    name = name.split()
    abbrev = []
    for i in range(len(name)):
        abbrev.append(name[i][0])
    return '.'.join(abbrev).upper()


print(abbrev_name('Victor Andrade'))