#!/usr/bin/python3

N = 15

def decide(field, i, j, position, N, OX):
    field[i][j] = OX
    if CanHaveNStones(field, position, N, OX):
        if OX == 'O':
            DebugPrint('choice at (%d, %d)' % (i, j))
        else:
            DebugPrint('block at (%d, %d)' % (i, j))
            field[i][j] = '.'
        return True
    field[i][j] = '.'
    return False

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))


    best_position = [(0, 0), 100]
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue

            position = (i, j)

            if decide(field, i, j, position, 5, 'O'):
                return position

            if decide(field, i, j, position, 5, 'X'):
                best_position = [position, 0]

            if decide(field, i, j, position, 4, 'O'):
                p = 1
                if best_position[1] > p:
                    best_position = [position, p]

            if decide(field, i, j, position, 4, 'X'):
                p = 2
                if best_position[1] > p:
                    best_position = [position, p]

            # Revert the assumption.
            if best_position[1] == 100:
                field[i][j] = '.'
                if GetDistance(best_position[0], CENTER) > GetDistance(position, CENTER):
                    best_position[0] = position
    for i in field:
        DebugPrint(*i)
    return best_position[0]


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveNStones(field, position, N, OX):
    return (CountStonesOnLine(field, position, (1, 1), OX) >= N or
            CountStonesOnLine(field, position, (1, 0), OX) >= N or
            CountStonesOnLine(field, position, (1, -1), OX) >= N or
            CountStonesOnLine(field, position, (0, 1), OX) >= N)


# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountStonesOnLine(field, position, diff, OX):
    count = 0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != OX:
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != OX:
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

