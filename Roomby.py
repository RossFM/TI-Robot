from array import *

room = [ [-1]*5  for n in range(5)] # Room is 2D array of of size 5x5
room[0][0] = 1
room[4][4] = 1

x,y = 0,0

print(x,y)

def split(directions):
    return list(directions)

inst = "NNESEESWNWW"

for char in split(inst):
    if char == "N":
        x = x + 1
    if char == "E":
        y = y + 1
    if char == "S":
        x = x - 1
    if char == "W":
        y = y - 1

for row in room:
    for col in row:
        print(x,y)
