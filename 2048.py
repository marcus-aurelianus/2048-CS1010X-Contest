#
# CS1010X --- Programming Methodology
#
# Module Instructor: Prof Ben 


from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]

##################
# Create Blocks  #
##################

def new_game_matrix(n):
    matrix=[]
    for i in range (n):
        matrix.append([0]*n)
    return matrix
   
def has_zero(mat):
    flat_mat=flatten(mat)
    return 0 in flat_mat

def add_two(mat):
    if has_zero(mat):
        indicator=1
        while indicator==1:
            pos=randint(0,len(mat)**2-1)
            row=pos%len(mat)
            col=pos//len(mat)
            if mat[row][col]==0:
                mat[row][col]=2
                indicator=0
    return mat

################
# game_status  #
################
def adjacent_not_same(mat):
    len1=len(mat)
    for i in range (len1-1):
        for j in range (len1):
            if mat[i][j]==mat[i+1][j] or mat[j][i]==mat[j][i+1]:
                return False
    return True
def game_status(mat):
    flat_mat=flatten(mat)
    if max(flat_mat)==2048:
        return "win"
    elif not has_zero(mat) and adjacent_not_same(mat):
        return "lose"
    else:
        return "not over"

#############
# Transpose #
#############

def transpose(mat):
    result=[]
    for i in range(len(mat[0])):
        result.append(list(map(lambda x:x[i],mat)))
    return result


#print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
#print(transpose([[1,2,3],[4,5,6]]))


###########
# Reverse #
###########

def reverse(mat):
    result=[]
    for i in range (len(mat)):
        result.append(mat[i][::-1])
    return result
#print(reverse([[1,2,3],[4,5,6],[7,8,9]]))
#print(reverse([[1,2,3],[4,5,6]]))

############
#   Merge  #
############

def merge_left(mat):
    score=0
    is_valid=False
    for row in range (len(mat)):
        for col in range(len(mat)):
            if mat[row][col] != 0:
                temp_col=col
                if (temp_col==len(mat)-1 or sum(mat[row][(temp_col+1):])==0):
                    while temp_col>0 and mat[row][temp_col-1]==0:
                        mat[row][temp_col],mat[row][temp_col-1]=mat[row][temp_col-1],mat[row][temp_col]
                        is_valid=True
                        temp_col-=1
                else:
                    next_col=temp_col+1
                    key=1
                    while next_col<=len(mat)-1 and key==1:
                        if mat[row][next_col]!=0:
                            key=0
                        if mat[row][temp_col]==mat[row][next_col]:
                            mat[row][temp_col],mat[row][next_col]=mat[row][temp_col]*2,0
                            is_valid=True
                            score+=mat[row][temp_col]
                        next_col+=1
                    while temp_col>0 and mat[row][temp_col-1]==0:
                        mat[row][temp_col],mat[row][temp_col-1]=mat[row][temp_col-1],mat[row][temp_col]
                        temp_col-=1

    return (mat,is_valid,score)
                       
#print(merge_left([[2,0,0,0],[0,0,0,0],[0,0,0,0],[2,0,0,0]]))                   
#print(merge_left([[0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0]]))                   



#############
#    Merge  #
#############

def merge_right(mat):
    mat_reverse=reverse(mat)
    new_mat=merge_left(mat_reverse)
    result=(reverse(new_mat[0]),new_mat[1],new_mat[2])
    return result
#print(merge_right([[2,0,2,2],[0,0,0,4],[0,4,8,4],[2,0,0,0]])) 

def merge_up(mat):
    mat_transpose=transpose(mat)
    new_mat=merge_left(mat_transpose)
    result=(transpose(new_mat[0]),new_mat[1],new_mat[2])
    return result

def merge_down(mat):
    mat_transpose=transpose(mat)
    new_mat=merge_right(mat_transpose)
    result=(transpose(new_mat[0]),new_mat[1],new_mat[2])
    return result


#############
# Text Game #
#############

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer: 1)Play the game till I win. 2) Play the game till I lose, then I know the if clause on status works. Though the second test is easier, I have tried both and they work.
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    "Your answer here"

def get_matrix(state):
    "Your answer here"

def get_score(state):
    "Your answer here"

def make_new_game(n):
    "Your answer here"

def left(state):
    "Your answer here"

def right(state):
    "Your answer here"

def up(state):
    "Your answer here"

def down(state):
    "Your answer here"


# Do not edit this #
#game_logic = {
#    'make_new_game': make_new_game,
#    'game_status': game_status,
#    'get_score': get_score,
#    'get_matrix': get_matrix,
#    'up': up,
#    'down': down,
#    'left': left,
#    'right': right,
#    'undo': lambda state: (state, False)
#}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
# gamegrid = GameGrid(game_logic)




#################
#   With Undo   #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return [mat,increment]

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############

def make_new_records():
    return []

def push_record(new_record, stack_of_records):
    stack_of_records.append(new_record)
    return stack_of_record

def is_empty(stack_of_records):
    return stack_of_records==[]

def pop_record(stack_of_records):
    last_record=stack_of_records.pop()
    return last_record

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return (matrix,total_score,records)

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    mat=add_two(add_two(new_game_matrix(n)))
    record=make_new_records()
    return make_state(mat,0,record)

def left(state):
    matrix=get_matrix(state)
    new_matrix_result=merge_left(matrix)
    new_matrix=new_matrix_result[0]
    valid_move=new_matrix_result[1]
    increment=(new_matrix_result[2])
    score=get_score(state)+increment
    record=make_new_record(matrix, increment)
    records=get_records(state)
    records.append(record)
    if valid_move:
        new_matrix=add_two(new_matrix)
    return (make_state(new_matrix,score,records),valid_move)

def right(state):
    matrix=get_matrix(state)
    new_matrix_result=merge_right(matrix)
    new_matrix=new_matrix_result[0]
    valid_move=new_matrix_result[1]
    increment=(new_matrix_result[2])
    score=get_score(state)+increment
    record=make_new_record(matrix, increment)
    records=get_records(state)
    records.append(record)
    if valid_move:
        new_matrix=add_two(new_matrix)
    return (make_state(new_matrix,score,records),valid_move)

def up(state):
    matrix=get_matrix(state)
    new_matrix_result=merge_up(matrix)
    new_matrix=new_matrix_result[0]
    valid_move=new_matrix_result[1]
    increment=(new_matrix_result[2])
    score=get_score(state)+increment
    record=make_new_record(matrix, increment)
    records=get_records(state)
    records.append(record)
    if valid_move:
        new_matrix=add_two(new_matrix)
    return (make_state(new_matrix,score,records),valid_move)

def down(state):
    matrix=get_matrix(state)
    new_matrix_result=merge_down(matrix)
    new_matrix=new_matrix_result[0]
    valid_move=new_matrix_result[1]
    increment=(new_matrix_result[2])
    score=get_score(state)+increment
    record=make_new_record(matrix, increment)
    records=get_records(state)
    records.append(record)
    if valid_move:
        new_matrix=add_two(new_matrix)
    return (make_state(new_matrix,score,records),valid_move)

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    return state[2]

def undo(state):
    stack_of_records=get_records(state)
    last_record=pop_record(stack_of_records)
    cur_score=get_score(state)
    score_increment=get_record_increment(last_record)
    prev_score=cur_score-score_increment
    prev_matrix=get_record_matrix(last_record)
    return (make_state(prev_matrix,prev_score,stack_of_records),True)


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': undo
}
gamegrid = GameGrid(game_logic)
