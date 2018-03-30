#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.


def Think(field):
    CENTER = (int(N / 2), int(N / 2))

    best_position = (0, 0)
    canMaxStone = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue
            position = (i, j)
            # Assume to put a stone on (i, j).
            
            field[i][j] = 'O'
            count, lineCounts = CanHaveFiveStones(field, position)
            #DebugPrint('I have a winning choice at (%d, %d)' %(i, j))
            if count >= 5:
                return position
            elif count > canMaxStone:
                best_position = position
                canMaxStone = count
                # return position
            field[i][j] = 'X'
            if OppHaveNumStones(field, position, 5):
                DebugPrint('I have a winning choice at (%d, %d)' % (i, j))
                return position
            field[i][j] = '.'
            if GetDistance(best_position, CENTER) > GetDistance(position, CENTER) and canMaxStone == 0:
                best_position = position
    return best_position

def tmpKinjite():
    cross = [(11, 11), (13, 11), (14, 11), (12, 12), (13, 12), (14, 12)]


def OppHaveNumStones(field, position, num):
    return (CountOppStonesOnLine(field, position, (1, 1)) >= num or
            CountOppStonesOnLine(field, position, (1, 0)) >= num or
            CountOppStonesOnLine(field, position, (1, -1)) >= num or
            CountOppStonesOnLine(field, position, (0, 1)) >= num)


def CountOppStonesOnLine(field, position, diff):
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

# Returns true if you have five stones from |position|. Returns false otherwise.


def CanHaveFiveStones(field, position):
    LineCounts = 0
    count1 = CountStonesOnLine(field, position, (1, 1))
    if LineCounts < CountStonesOnLine(field, position, (1, 1)):
        LineCounts = count1
    count2 = CountStonesOnLine(field, position, (1, 0))
    if LineCounts < CountStonesOnLine(field, position, (1, 0)):
        LineCounts = count2
    count3 = CountStonesOnLine(field, position, (0, 1))
    if LineCounts < CountStonesOnLine(field, position, (0, 1)):
        LineCounts = count3
    count4 = CountStonesOnLine(field, position, (1, -1))
    if LineCounts < CountStonesOnLine(field, position, (1, -1)):
        LineCounts = count4

    return LineCounts, (count1 * count2 * count3* count4)

    # return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
    #         CountStonesOnLine(field, position, (1, 0)) >= 5 or
    #         CountStonesOnLine(field, position, (1, -1)) >= 5 or
    #         CountStonesOnLine(field, position, (0, 1)) >= 5)


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
    #num = count
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


if __name__ == '__main__':
    main()

