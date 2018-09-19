#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def checkWinPosition(field, position):
    pass


def Think(field):
    CENTER = (int(N / 2), int(N / 2))


    best_position = (0, 0)
    priority=0
    best_priority=(priority, best_position)
    
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue

            position = (i, j)
            
            #check opponent position
            field[i][j] = 'X'
            if CanOpponentHaveThreeStones(field, position):
                field[i][j] = 'O'
                DebugPrint('CanOpponentHaveThreeStones (%d, %d)' % (i, j))
                priority=10
                best_priority=(priority, position)
                
                #return position
            else:
                #field[i][j] = '.'    
                # Assume to put a stone on (i, j).
                field[i][j] = 'O'

                if CanHaveFiveStones(field, position):
                    #DebugPrint('CanHaveFiveStones (%d, %d)' % (i, j))
                    priority=8
                    if (priority>best_priority[0]):
                        best_priority=(priority, position)
                    #return position
                if CanHaveThreeStones(field, position) :
                    #DebugPrint('CanHaveThreeStones(%d, %d)' % (i, j))
                    priority=7
                    if (priority>best_priority[0]):
                        best_priority=(priority, position)

                    #best_position = 
                if CanHaveTwoStones(field, position) :
                    priority=5
                    if (priority>best_priority[0]):
                        best_priority=(priority, position)
                    #DebugPrint('CanHaveThreeStones(%d, %d)' % (i, j))
                    #return position
                # Revert the assumption.
                field[i][j] = '.'
                if GetDistance(best_priority[1], CENTER) > GetDistance(position, CENTER):
                    priority=1
                    if (priority>=best_priority[0]):
                        best_priority=(priority, position)
    return best_priority[1]


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
            CountStonesOnLine(field, position, (1, 0)) >= 5 or
            CountStonesOnLine(field, position, (1, -1)) >= 5 or
            CountStonesOnLine(field, position, (0, 1)) >= 5)

def CanHaveTwoStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 3 or
            CountStonesOnLine(field, position, (1, 0)) >= 3 or
            CountStonesOnLine(field, position, (1, -1)) >= 3 or
            CountStonesOnLine(field, position, (0, 1)) >= 3)



def CanHaveThreeStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 4 or
            CountStonesOnLine(field, position, (1, 0)) >= 4 or
            CountStonesOnLine(field, position, (1, -1)) >= 4 or
            CountStonesOnLine(field, position, (0, 1)) >= 4)


def CanOpponentHaveThreeStones(field, position):
    return (CountOppopnetnStonesOnLine(field, position, (1, 1)) >= 4 or
            CountOppopnetnStonesOnLine(field, position, (1, 0)) >= 4 or
            CountOppopnetnStonesOnLine(field, position, (1, -1)) >= 4 or
            CountOppopnetnStonesOnLine(field, position, (0, 1)) >= 4)


# Returns the number of stones you can put around |position| in the direction specified by |diff|.
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


# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountStonesAndEmptyOnLine(field, position, diff):
    count = 0
    stones=0
    empty=0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            break
        #if field[row][col] != 'O'
        row += diff[0]
        col += diff[1]
        stones += 1


    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            break
        row -= diff[0]
        col -= diff[1]
        count += 1

    return count

# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountOppopnetnStonesOnLine(field, position, diff):
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

    #DebugPrint('CanOpponentHave count (%d: %d, %d)' % (count, position[0], position[1]))

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

