"""

Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

"""

def tower_builder(n_floors):
    
    tower = []

    floors = 0
    i = 0
    while floors != n_floors:
        brick = '*' * (i+1)
        if (i+1) % 2 == 0:
            i += 1
        else:
            tower.append(brick.center((1 + (n_floors-1)*2), ' '))
            i += 1
            floors += 1
    
    return tower

print(tower_builder(5))

    