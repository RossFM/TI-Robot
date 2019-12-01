import sys

try:
    input = open("input.txt", "r") #Read input file from current directory

    if input.mode == 'r': #if in read mode, read the file
        contents = input.read()
        data = contents.split('\n') #Create a list, each new line in the file being an element

    roomx,roomy = list(map(int, data[0].split())) #Room Dimension - from first line of input
    x,y = list(map(int, data[1].split())) #Starting position of hoover, second line of input
    del data[0] #Remove room dimension line from data
    del data[0] #Remove hoover position from data
except Exception as e:
    sys.exit("Input not formatted as expected, please check and try again")

dirt = [] #init list for dirt positions
dir = '' #init sting for directions

for items in data:
    try: #Propogate dirt list with remaining elements of data, converted to type int
        dirt.append(list(map(int, items.split())))
    except ValueError:
        dir = items #if an element fails to convert to int, its the directions
dirt.pop() #Remove empty list element

def split(directions):
    return list(directions) #Split directions into individual chars

cleanedAreas = 0
for char in split(dir): #Turn each meaningful char instruction into movement of the hover
    if char == "N":
        y = y + 1
    elif char == "E":
        x = x + 1
    elif char == "S":
        y = y - 1
    elif char == "W":
        x = x - 1
    else: #Catch and discard any invalid directions
        print("Invalid direction in input file. Will ignore and continue")
    if x > roomx: #if hoover reaches the edges of the room it skids in place
        x = x - 1
    if x < 0:
        x = x +1
    if y > roomy:
        y = y - 1
    if y < 0:
        y = y + 1

    for dust in dirt: #if a hoover movement reaches a piece of dirt...
        if [x,y] == dust:
            dust.pop() #"Hoover" up piece of dirt from room
            cleanedAreas = cleanedAreas + 1 #add one to count of cleaned areas

print(x,y, "\n", cleanedAreas)
