#!/usr/bin/python3

N = 15

TURN_COUNT = 0

# turnCOUNT = 0

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):

    global TURN_COUNT

    CENTER = (int(N / 2), int(N / 2))

    # ターン数
    TURN_COUNT = TURN_COUNT + 1
    DebugPrint(TURN_COUNT)

    best_position = (0, 0)
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue

            if field[i][j] == 'X'

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

            for n in reversed(range(5)):
                if CanHaveStones(field, position, n):
                    best_position = position


    return best_position


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
            CountStonesOnLine(field, position, (1, 0)) >= 5 or
            CountStonesOnLine(field, position, (1, -1)) >= 5 or
            CountStonesOnLine(field, position, (0, 1)) >= 5)

# TODO ORIGINAL
def CanHaveStones(field, position, num):
    return (CountStonesOnLine(field, position, (1, 1)) >= num or
            CountStonesOnLine(field, position, (1, 0)) >= num or
            CountStonesOnLine(field, position, (1, -1)) >= num or
            CountStonesOnLine(field, position, (0, 1)) >= num)


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

# GET POSITION
def getPosition(field, position, diff):
    count = 0
    enemy_list

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            enemy_list.append((row, col))
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            enemy_list.append((row, col))
            break
        row -= diff[0]
        col -= diff[1]
        count += 1

    enemy_list.insert(0, count)

    return enemy_list

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
