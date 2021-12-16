# 1 2 3 | 00 01 02
# 4 5 6 | 10 11 12
# 7 8 ? | 20 21 22
#values | coordinates

#inputs

#coordinates
#value <1-8>
#bool occupied or not

import numpy as np

#bool matrix
is_occupied_bool_matrix = np.array([[False, False, False], [False, False, False], [False, False, False]])
"""
#start state representation matrix
start_state_representation_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

#goal state representation matrix
goal_state_representation_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
"""
#delete this block before build::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#test case_1

#start state representation matrix
start_state_representation_matrix = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])

#goal state representation matrix
goal_state_representation_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

#loop to assign bools into is_occupied_bool_matrix
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        if start_state_representation_matrix[i][j] != 0:
            #print("occupied")
            is_occupied_bool_matrix[i][j] = True
        #print(np.where(start_state_representation_matrix == i))
        #is_occupied_bool_matrix
print("is occupied bool matrix is{}".format(is_occupied_bool_matrix))
#delete the above:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
#take inputs for start state matrix
i = 0
while i <= 7:
    print("for start state only")
    x, y, value = input("enter coordinates and value in X Y V format").split(' ')
    x = int(x); y = int(y); value = int(value)
    if value > 8 or value < 1:
        value = input("wrong V input enter V again")
    else:
        print("X Y & V are {}, {}, {}".format(x, y, value))
        start_state_representation_matrix[x,y] = value
        if start_state_representation_matrix[x,y] != 0:
            is_occupied_bool_matrix[x,y] = True
    i = i + 1
print(start_state_representation_matrix)
print(is_occupied_bool_matrix)

#take inputs for goal state matrix
i = 0
while i <= 7:
    print("for goal state only")
    x, y, value = input("enter coordinates and value in X Y V format").split(' ')
    x = int(x); y = int(y); value = int(value)
    if value > 8 or value < 1:
        value = input("wrong V input enter V again")
    else:
        print("X Y & V are {}, {}, {}".format(x, y, value))
        goal_state_representation_matrix[x,y] = value
    i = i + 1
print(goal_state_representation_matrix)
"""
print("is start state = goal state \n{}".format(start_state_representation_matrix == goal_state_representation_matrix))

#is misplaced matrix
is_misplaced_matrix = (start_state_representation_matrix != goal_state_representation_matrix)

print("is misplaced matrix is \n{}".format(is_misplaced_matrix))


"""
moving tiles

conditions::
1) move only if the position of that pirticular tile doesn't satisfy the goal state
2) move only one tile either to RIGHT LEFT TOP BOTTOM once only for each iteration

"""

#moving tiles
"""

first access the tile
first check weather the tile is at right position or not
if it is not at right position
    check if void is present next to it
    if void is present next to it
        check direction of void (void == 0)
        if void is at right move right, else move correspodingly
    else
        transition to next tile
else
    leave it
    transition to next tile

"""
#i = input("enter 2")
count = 0
heat = 0
visited_address = []
while start_state_representation_matrix.all() == goal_state_representation_matrix.all() and count < 100:
#access tile "0" from start state matrix and move it!
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            tile = start_state_representation_matrix[i][j]
            if tile == 0:
                cX = i; cY = j
                s_cX = str(cX); s_cY = str(cY)
                visited_address.append(s_cX+s_cY)
            
                if cX + 1 <= 2 and heat != 2: #(str(cX + 1) + str(cY)) not in visited_address:     #move down
                    start_state_representation_matrix[cX][cY], start_state_representation_matrix[cX + 1][cY] = start_state_representation_matrix[cX + 1][cY], start_state_representation_matrix[cX][cY]
                    heat = 1
                elif cX - 1 >= 0 and heat != 1: #(str(cX - 1) + str(cY)) not in visited_address:   #move up
                    start_state_representation_matrix[cX][cY], start_state_representation_matrix[cX - 1][cY] = start_state_representation_matrix[cX - 1][cY], start_state_representation_matrix[cX][cY]
                    heat = 2
                elif cY + 1 <= 2 and heat != 4: #(str(cX) + str(cY + 1)) not in visited_address:   #move right
                    start_state_representation_matrix[cX][cY], start_state_representation_matrix[cX][cY + 1] = start_state_representation_matrix[cX][cY + 1], start_state_representation_matrix[cX][cY]
                    heat = 3
                elif cY - 1 >= 0 and heat != 3: #(str(cX) + str(cY - 1)) not in visited_address:   #move left
                    start_state_representation_matrix[cX][cY], start_state_representation_matrix[cX][cY - 1] = start_state_representation_matrix[cX][cY - 1], start_state_representation_matrix[cX][cY]
                    heat = 4
            #print updated start_state_representation_matrix

                print("start state matrix updated [{}] [{}] \n{}".format(i, j, start_state_representation_matrix))
        #if is_misplaced_matrix[i][j] == False:

            #do nothing
         #   continue
        #else:
            #do something
            # check if the tile is zero
            # move zero
            #if 
    count = count + 1
    print(count)
"""
#tile moving functions

#function to move tile up
def moveUp():
    print("none")
#function to move tile down
def moveDown():
    print("none")
#function to move tile right
def moveRight():
    print("none")
#funtion to move tile left
def moveLeft():
    print("none")
"""
