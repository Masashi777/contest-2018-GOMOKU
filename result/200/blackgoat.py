#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))
    flg=0
    flg2=0
    best_position = (0, 0)
    best_position2 = (-1,-1)
    best_position3 = (-1,-1)
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue
            position = (i, j)
            #Assume to put a stone on (i,j) as opponent 対戦相手
            field[i][j]='X'
            # for k in range(N):
            #    for l in range(N):
            #        hoge = (k,l)
            #        if DoHaveNStones(field,hoge,5,'X'):
            #            DebugPrint('pinch')
            #            DebugPrint(hoge)
            if DoHaveNStones(field,position,5,'X'):
                        DebugPrint('pinch')
                        DebugPrint(position)
                        best_position3=position
    
            # Assume to put a stone on (i, j).
            field[i][j] = 'O'

            if DoHaveNStones(field, position,5,'O'):
                DebugPrint('I have a winning choice at (%d, %d)' % (i, j))
                return position
            if DoHaveNStones(field,position,4,'O'):
                DebugPrint('I have a three stones at (%d, %d)' % (i,j))
                best_position=position
                flg=1
            if DoHaveNStones(field,position,3,'X') or DoHaveNStones(field,position,4,'X'):
                DebugPrint('I need to stop at (%d, %d)' % (i,j))
                flg2=1
                if GetDistance(best_position2, CENTER) > GetDistance(position, CENTER):
                    best_position2=position

            # Revert the assumption.
            field[i][j] = '.'
            if flg!=1 and flg2!=1 and GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                best_position = position
    if(best_position3!=(-1,-1)):
        return best_position3
    if(best_position2!=(-1,-1)):
        DebugPrint("no")
        return best_position2
    return best_position

#returns truee if you have a three-stones line from |position|.Returns false otherwise.
def DoHaveNStones(field,position,N,player):
    if(player=='X'):
        return (CountStonesOnLineX(field, position, (1, 1)) >= N or
                CountStonesOnLineX(field, position, (1, 0)) >= N or
                CountStonesOnLineX(field, position, (1, -1)) >= N or
                CountStonesOnLineX(field, position, (-1, 1)) >= N or
                CountStonesOnLineX(field, position, (-1, 0)) >= N or
                CountStonesOnLineX(field, position, (-1, -1)) >= N or
                CountStonesOnLineX(field, position, (0, -1)) >= N or
                CountStonesOnLineX(field, position, (0, 1)) >= N
                )
    else:
          return (CountStonesOnLine(field, position, (1, 1)) >= N or
                CountStonesOnLine(field, position, (1, 0)) >= N or
                CountStonesOnLine(field, position, (1, -1)) >= N or
                CountStonesOnLine(field, position, (-1, 1)) >= N or
                CountStonesOnLine(field, position, (-1, 0)) >= N or
                CountStonesOnLine(field, position, (-1, -1)) >= N or
                CountStonesOnLine(field, position, (0, -1)) >= N or
                CountStonesOnLine(field, position, (0, 1)) >= N
                )

# Returns true if you have a five-stones line from |position|. Returns false otherwise.
def DoHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
            CountStonesOnLine(field, position, (1, 0)) >= 5 or
            CountStonesOnLine(field, position, (1, -1)) >= 5 or
            CountStonesOnLine(field, position, (0, 1)) >= 5)


# Returns the number of stones on the line segment on the direction of |diff| from |position|.
def CountStonesOnLine(field, position, diff):
    count = 0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            break
        row -= diff[0]
        col -= diff[1]
        count += 1

    return count

# Returns the number of stones on the line segment on the direction of |diff| from |position|.
def CountStonesOnLineX(field, position, diff):
    count = 0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'X':
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'X':
            break
        row -= diff[0]
        col -= diff[1]
        count += 1

    return count

# Returns the Manhattan distance from |a| to |b|.
def GetDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Outputs |msg| to stderr; This is actually a thin wrapper of print().
def DebugPrint(msg):
    import sys
    print(msg, file=sys.stderr)


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

if __name__    == '__main__':
    main()



