#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))

    best_position = (0, 0)
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
            field[i][j] = '.'
            if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                best_position = position

    my_position = Judge4stone(i,j, field)
    if my_position != 0:
        DebugPrint('!')
        best_position = my_position


    my_position = JudgeEnemy4(i,j, field)
    if my_position != 0:
        best_position = my_position

    my_position = JudgeEnemySlanting(i,j, field)
    if my_position != 0:
        DebugPrint('damee')
        best_position = my_position

    my_position = JudgeEnemy5(i,j, field)
    if my_position != 0:
        DebugPrint('damee')
        best_position = my_position

    my_position = JudgeSlanting(i,j, field)
    if my_position != 0:
        best_position = my_position

    my_position = Judge5stone(i,j, field)
    if my_position != 0:
        best_position = my_position

    return best_position


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
            CountStonesOnLine(field, position, (1, 0)) >= 5 or
            CountStonesOnLine(field, position, (1, -1)) >= 5 or
            CountStonesOnLine(field, position, (0, 1)) >= 5)


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


# Returns the Manhattan distance from |a| to |b|.
def GetDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def Judge5stone(orig_i, orig_j, field):
    for j in range(15):
        for i in range(10):
            count_x = 0;
            vacantpos = 0;
            for k in range(5):
                if field[i+k][j] == 'O':
                    count_x += 1
                if field[i+k][j] == '.':
                    vacantpos = k+i
                if field[i+k][j] == 'X':
                    count_x = 0
            if count_x == 4:
                return (vacantpos, j)


    for j in range(15):
        for i in range(10):
            count_x = 0;
            vacantpos = 0;
            for k in range(5):
                if field[j][i+k] == 'O':
                    count_x += 1
                if field[j][i+k] == '.':
                    vacantpos = k+i
                if field[j][i+k] == 'X':
                    count_x = 0
            if count_x == 4:
                return (j, vacantpos)


    return 0

def Judge4stone(orig_i, orig_j,field):
    for j in range(15):
        for i in range(11):
            count_x = 0;
            vacantpos = 0;
            for k in range(4):
                if field[i+k][j] == 'O':
                    count_x += 1
                if field[i+k][j] == '.':
                    vacantpos = k+i
                if field[i+k][j] == 'X':
                    count_x = -1
            if count_x == 3:
                return (vacantpos, j)

    for j in range(15):
        for i in range(11):
            count_x = 0;
            vacantpos = 0;
            for k in range(4):
                if field[j][i+k] == 'O':
                    count_x += 1
                if field[j][i+k] == '.':
                    vacantpos = k+i
                if field[j][i+k] == 'X':
                    count_x = -1
            if count_x == 3:
                return (j, vacantpos)

    return 0

def JudgeSlanting(orig_i, orig_j, field):
    for j in range(11):
        for i in range(11):
            count_x = 0;
            vacantpos_k = 0;
            for k in range(5):
                if field[i+k][j+k] == 'O':
                    count_x += 1
                if field[i+k][j+k] == '.':
                    vacantpos_k = k
                if field[i+k][j+k] == 'X':
                    count_x = -1
            if count_x == 4:
                return (i+vacantpos_k, j+vacantpos_k)

    for j in range(11):
        for i in range(5, 15):
            count_x = 0;
            vacantpos_k = 0;
            for k in range(5):
                if field[i-k][j+k] == 'O':
                    count_x += 1
                if field[i-k][j+k] == '.':
                    vacantpos_k = k
                if field[i-k][j+k] == 'X':
                    count_x = -1
            if count_x == 4:
                return (i-vacantpos_k, j+vacantpos_k)

    return 0

def JudgeEnemySlanting(orig_i, orig_j, field):
    for j in range(10):
        for i in range(10):
            count_x = 0;
            vacantpos_k = 0;
            for k in range(5):
                if field[i+k][j+k] == 'X':
                    count_x += 1
                if field[i+k][j+k] == '.':
                    vacantpos_k = k
                if field[i+k][j+k] == 'O':
                    count_x = -1
            if count_x == 4:
                return (i+vacantpos_k, j+vacantpos_k)

    for j in range(11):
        for i in range(5, 15):
            count_x = 0;
            vacantpos_k = 0;
            for k in range(5):
                if field[i-k][j+k] == 'X':
                    count_x += 1
                if field[i-k][j+k] == '.':
                    vacantpos_k = k
                if field[i-k][j+k] == 'O':
                    count_x = -1
            if count_x == 4:
                return (i-vacantpos_k, j+vacantpos_k)

    return 0

def JudgeEnemy4Slanting(orig_i, orig_j, field):
    for j in range(11):
        for i in range(11):
            count_x = 0;
            vacantpos_k = 0;
            for k in range(4):
                if field[i+k][j+k] == 'X':
                    count_x += 1
                if field[i+k][j+k] == '.':
                    vacantpos_k = k
                if field[i+k][j+k] == 'O':
                    count_x = -1
            if count_x == 3:
                return (i+vacantpos_k, j+vacantpos_k)

    for j in range(11):
        for i in range(4, 15):
            count_x = 0;
            vacantpos_k = 0;
            for k in range(4):
                if field[i-k][j+k] == 'X':
                    count_x += 1
                if field[i-k][j+k] == '.':
                    vacantpos_k = k
                if field[i-k][j+k] == 'O':
                    count_x = -1
            if count_x == 3:
                return (i-vacantpos_k, j+vacantpos_k)

    return 0


def JudgeEnemy5(orig_i, orig_j, field):
    DebugPrint('dame')
    for j in range(15):
        for i in range(10):
            count_x = 0;
            vacantpos = 0;
            for k in range(5):
                if field[i+k][j] == 'X':
                    count_x += 1
                if field[i+k][j] == '.':
                    vacantpos = k+i
                if field[i+k][j] == 'O':
                    count_x = 0
            if count_x == 4:
                return (vacantpos, j)

    for j in range(15):
        for i in range(10):
            count_x = 0;
            vacantpos = 0;
            for k in range(5):
                if field[j][i+k] == 'X':
                    count_x += 1
                if field[j][i+k] == '.':
                    vacantpos = k+i
                if field[j][i+k] == 'O':
                    count_x = 0
            if count_x == 4:
                return (j, vacantpos)

    return 0

def JudgeEnemy4(orig_i, orig_j, field):
    DebugPrint('dame')
    for j in range(15):
        for i in range(11):
            count_x = 0;
            vacantpos = 0;
            for k in range(4):
                if field[i+k][j] == 'X':
                    count_x += 1
                if field[i+k][j] == '.':
                    vacantpos = k+i
                if field[i+k][j] == 'O':
                    count_x = -1
            if count_x == 3:
                return (vacantpos, j)

    for j in range(15):
        for i in range(11):
            count_x = 0;
            vacantpos = 0;
            for k in range(4):
                if field[j][i+k] == 'X':
                    count_x += 1
                if field[j][i+k] == '.':
                    vacantpos = k+i
                if field[j][i+k] == 'O':
                    count_x = -1
            if count_x == 3:
                return (j, vacantpos)

    return 0

def JudgeEnemy3(arg):
    pass


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

