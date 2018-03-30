#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))
    best_position = (0,0)
    x =[]
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue

            position = (i, j)
            # Assume to put a stone on (i, j).
            field[i][j] = 'O'
            if CanHaveFiveStones(field, position):
                DebugPrint('I have a winning choice at (%d, %d)' % (i, j))
                return position
            # Revert the assumption.
            field[i][j] = 'X'
            #CHECK THE RIVAL 
            if CanHaveFourCrosses(field,position):
                return position
            field[i][j] ='.'
                
            if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                best_position = position
                del x[:]
                x.append(position)
            if GetDistance(best_position,CENTER) == GetDistance(position,CENTER):
                x.append(position)
    min_x =9
    for y in x:
        curr_x = CountNumX(field, y)
        if(curr_x <min_x):
            best_position = y
            min_x = curr_x
    return best_position

def CountNumX(field, position):
    row = position[0]
    col = position[1]
    counter = 0
    ### Check UP 
    if(row>0 and field[row-1][col] == 'X'):
        counter += 1
    ###Down 
    if(row < N-1 and field[row+1][col] =='X'):
        counter +=1
    ###Left 
    if(col > 0 and field[row][col-1] =='X'):
        counter +=1
    ###Right
    if(col < N-1 and field[row][col+1] =='X'):
        counter +=1
    ### CHeck the diagonals 
    if(row >0 and col >0) :
        if(field[row-1][col-1] =='X'):
            counter +=1
    if(row>0 and col < N-1):
        if(field[row-1][col+1] =='X'):
            counter +=1
    if(row < N-1 and col >0):
        if(field[row+1][col-1] =='X'):
            counter +=1
    if(row <N-1 and col <N-1):
        if(field[row+1][col+1] =='X'):
            counter +=1
    return counter

def CanHaveFourCrosses(field, position):
    return (CountStonesOnLine(field, position, (1, 1) ,'X') >= 3 or
            CountStonesOnLine(field, position, (1, 0),'X') >= 3 or
            CountStonesOnLine(field, position, (1, -1),'X') >= 3 or
            CountStonesOnLine(field, position, (0, 1),'X') >= 3)


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1), '0') >= 5 or
            CountStonesOnLine(field, position, (1, 0), '0') >= 5 or
            CountStonesOnLine(field, position, (1, -1), '0') >= 5 or
            CountStonesOnLine(field, position, (0, 1), '0') >= 5)


# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountStonesOnLine(field, position, diff ,c):
    count = 0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != c:
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != c:
            break
        row -= diff[0]
        col -= diff[1]
        count += 1

    return count


# Returns the Manhattan distance from |a| to |b|.
def GetDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# =============================================================================
# DO NOT EDIT FOLLOWING FUNCTIONS
# =============================================================================

def main():
    field = Input()
    position = Think(field)
    Output(position)


def Input():
    field = [list(input()) for i in range(N)]
    return field


def Output(position):
    print(position[0], position[1])


# Outputs |msg| to stderr; This is actually a thin wrapper of print().
def DebugPrint(*msg):
    import sys
    print(*msg, file=sys.stderr)


if __name__    == '__main__':
    main()
