
#import numpy as np
def equalList(list_1, list_2):
    for element in list_1:
        list_2.append(element)
    return(list_2)
start_state_matrix = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
#start_state_matrix = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
#goal_state_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
goal_state_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#temp_state_matrix = start_state_matrix
temp_state_matrix = []
equalList(start_state_matrix, temp_state_matrix)

states_matrix_array = []
states_matrix_array.append(start_state_matrix)
moves = ['up', 'down', 'left', 'right']
possible_moves = ['none', 'none', 'none']



def returnPossibleMove(i, j): #returns possible moves
    moves = ['up', 'down', 'left', 'right']
    possible_moves = ['none', 'none', 'none']
    if i == 0:
        moves.pop(moves.index('up'))
    if i == 2:
        moves.pop(moves.index('down'))
    if j == 0:
        moves.pop(moves.index('left'))
    if j == 2:
        moves.pop(moves.index('right'))
    return(moves)

def findVoidLoc(temp_matrix):  #finds location of void (zero) and returns possible moves  
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if temp_matrix[i][j] == 0:
                cX = i; cY = 0
                #print("found 0")
                possible_moves = returnPossibleMove(cX, cY)
                #print(possible_moves)
                return(cX, cY, possible_moves)

def moveUp(matrix, coordX, coordY):
    matrix[coordX][coordY], matrix[coordX - 1][coordY] = matrix[coordX - 1][coordY], matrix[coordX][coordY]
    return(matrix)
def moveDown(matrix, coordX, coordY):
    matrix[coordX][coordY], matrix[coordX + 1][coordY] = matrix[coordX + 1][coordY], matrix[coordX][coordY]
    return(matrix)
def moveRight(matrix, coordX, coordY):
    matrix[coordX][coordY], matrix[coordX][coordY + 1] = matrix[coordX][coordY + 1], matrix[coordX][coordY]
    return(matrix)
def moveLeft(matrix, coordX, coordY):
    matrix[coordX][coordY], matrix[coordX][coordY - 1] = matrix[coordX][coordY - 1], matrix[coordX][coordY]
    return(matrix)
x = []
equalList(temp_state_matrix, x)

cX, cY, possible_moves = findVoidLoc(x)
print("location of void is ({}, {}) \n and possible moves are: {}".format(cX, cY, possible_moves))
def moveTile(move, xCoord, yCoord, toMove):   #move void
    #xCoord, yCoord = int(xCoord), int(yCoord)
    #print(type(xCoord))
    if move == 'up':
        #toMove[xCoord][yCoord], toMove[xCoord - 1][yCoord] = toMove[xCoord - 1][yCoord], toMove[xCoord][yCoord]
        moveUp(toMove, xCoord, yCoord)
        #return(toMove)
    elif move == 'down':
        #toMove[xCoord][yCoord], toMove[xCoord + 1][yCoord] = toMove[xCoord + 1][yCoord], toMove[xCoord][yCoord]
        #return(toMove)
        moveDown(toMove, xCoord, yCoord)
    elif move == 'right':
        #toMove[xCoord][yCoord], toMove[xCoord][yCoord + 1] = toMove[xCoord][yCoord + 1], toMove[xCoord][yCoord]
        #return(toMove)
        moveRight(toMove, xCoord, yCoord)
    elif move == 'left':
        #toMove[xCoord][yCoord], toMove[xCoord][yCoord - 1] = toMove[xCoord][yCoord - 1], toMove[xCoord][yCoord]
        #return(toMove)
        moveLeft(toMove, xCoord, yCoord)


#print(type(cX))
#moveTile('up', cX, cY, temp_state_matrix)

print(temp_state_matrix)
print(x)
#moveTile(possible_moves[0], cX, cY, x)
#moveUp(x, 2, 0)
print(x)
print(temp_state_matrix)

key = len(states_matrix_array)-1
node_Dictionary = {
    "key" : key,
    "parent" : states_matrix_array[key],
    "move" : 'none',
    "state" : start_state_matrix
}
#print(node_Dictionary)