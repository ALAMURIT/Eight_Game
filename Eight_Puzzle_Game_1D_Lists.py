# 1 2 3 | 0 1 2
# 4 5 6 | 3 4 5
# 7 8 0 | 6 7 8
# values| indices

#take inputs

print("""

sequence or order for giving inputs

# 1 2 3 | 0 1 2
# 4 5 6 | 3 4 5
# 7 8 0 | 6 7 8
# values| indices

# """)
start_state_matrix = []
goal_state_matrix = []
#start_state_matrix = [1, 2, 3, 4, 5, 6, 0, 7, 8]
#goal_state_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 0]
for a in range(0, 9):
    t = int(input("enter {}th element for start state of  puzzle".format(a)))
    start_state_matrix.append(t)
print(start_state_matrix)
#for a in range(0, 8, 1):
#    for c in range(0, 3, 1):
#        print(start_state_matrix[a])
#    print("\n")
for a in range(0, 9):
    t = int(input("enter {}th element for goal state of puzzle".format(a)))
    goal_state_matrix.append(t)
print(goal_state_matrix)
#for a in range(0, 8, 1):
#    for c in range(0, 3, 1):
#        print(goal_state_matrix[a])
#    print("\n")
#start_state_matrix = map(input("enter start state matrix"))

states_matrix = []
states_matrix.append(start_state_matrix)

def equalList(list_1, list_2):  #implies list_2 = list_1
    for element in list_1:
        list_2.append(element)
    return(list_2)

def equateList(list_1, list_2):
    k = 0
    for i in list_1:
        list_2[k] = i
        k=k+1
temp_matrix = []
equalList(states_matrix[0], temp_matrix)
moves = ['up', 'down', 'left', 'right']
possible_moves = ['none', 'none', 'none', 'none']

def findVoidLocation(test_matrix):  #returns the location of void ' 0 '
    for i in temp_matrix:
        if i == 0:
            return(temp_matrix.index(i))

def findPossibleMoves(void_location):   #returns the possible moves for given location of void
    moves = ['up', 'down', 'left', 'right']
    if void_location % 3 == 0:
        moves.pop(moves.index('left'))
    if void_location % 3 == 2:
        moves.pop(moves.index('right'))
    if void_location >= 0 and void_location <= 3:
        moves.pop(moves.index('up'))
    if void_location >= 6 and void_location <= 8:
        moves.pop(moves.index('down'))
    return(moves)

#print(findPossibleMoves(findVoidLocation(temp_matrix)))

def moveUp(void_location, input_matrix):    #returns matrix after moving void up
    input_matrix[void_location], input_matrix[void_location - 3] = input_matrix[void_location - 3], input_matrix[void_location]
    return(input_matrix)

def moveDown(void_location, input_matrix):    #returns matrix after moving void down
    input_matrix[void_location], input_matrix[void_location + 3] = input_matrix[void_location + 3], input_matrix[void_location]
    return(input_matrix)

def moveLeft(void_location, input_matrix):    #returns matrix after moving void left
    input_matrix[void_location], input_matrix[void_location - 1] = input_matrix[void_location - 1], input_matrix[void_location]
    return(input_matrix)

def moveRight(void_location, input_matrix):    #returns matrix after moving void right
    input_matrix[void_location], input_matrix[void_location + 1] = input_matrix[void_location + 1], input_matrix[void_location]
    return(input_matrix)

def moveTile(input_matrix, void_location, move):
    #temp_input_matrix = []
    #equalList(temp_input_matrix, input_matrix)
    if move == 'up':
        moveUp(void_location, input_matrix)
        return(input_matrix)
    
    if move == 'down':
        moveDown(void_location, input_matrix)
        return(input_matrix)
    
    if move == 'right':
        moveRight(void_location, input_matrix)
        return(input_matrix)
    
    if move == 'left':
        moveLeft(void_location, input_matrix)
        return(input_matrix)

nodes_dictionary = {
    "key" : 0,
    "parent" : states_matrix[0],
    #"moves" : findPossibleMoves(findVoidLocation(states_matrix[0]))
    #"child_index" : #child_index 
}

nodes_dictionary_list = []
nodes = [[1, 2, 3, 4, 5, 6, 0, 7, 8]]
epoch = 0
dummy_matrix = []
index = 0
outer_index = 0
#nodes.append(states_matrix[0])
equalList(start_state_matrix, dummy_matrix)
#equalList(start_state_matrix, dummy_matrix)
isBreakLoop = False
while start_state_matrix != goal_state_matrix and epoch <= 100 and isBreakLoop == False:
    nodes_dictionary_list = []
    #print(nodes[outer_index])
    #loc = findVoidLocation(nodes[outer_index])
    for element in nodes[outer_index]:
        if element == 0:
            loc = nodes[outer_index].index(0)
    print(nodes[outer_index])
    print(loc)
    for i in findPossibleMoves(loc):
        equateList(nodes[outer_index], temp_matrix)
        nodes.append([])
        equalList(moveTile(temp_matrix, loc, i), nodes[index + 1])
        print(nodes[index + 1], i)
        #nodes_dictionary.update({"key" : outer_index, "parent" : nodes[outer_index], "move" : i, "value" : nodes[index]})
        #nodes_dictionary_list.insert(outer_index, nodes_dictionary)
        if(nodes[index + 1]) == goal_state_matrix:
            print("got solution\n")
            isBreakLoop = True
        index = index + 1
    outer_index = outer_index + 1
    epoch = epoch + 1
    #equalList()
    #states_matrix.append(moveTile(temp_matrix, findVoidLocation(temp_matrix), i))
print(nodes)
print(nodes_dictionary_list)
