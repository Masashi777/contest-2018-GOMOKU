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

            #ごれんちゃんが完成するかを判定、そうでなかったら中心に近いところにおく
            if CanHaveFiveStones(field, position,5):
                DebugPrint('I have a winning choice at (%d, %d)' % (i, j))
                return position
            if CanHaveFiveStones(field, position,4):
                return position
            if CanHaveFiveStones(field, position,3):
                return position
            #if CanHaveFiveStones(field, position,2):
            #    return position


            # Revert the assumption.
            field[i][j] = '.'
            if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                best_position = position
    return best_position


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position,n):
    return (CountStonesOnLine(field, position, (1, 1)) >= n or
            CountStonesOnLine(field, position, (1, 0)) >= n or
            CountStonesOnLine(field, position, (1, -1)) >= n or
            CountStonesOnLine(field, position, (0, 1)) >= n)

def CanHaveFiveStonesonX(field, position,n):
    return (CountXOnLine(field, position, (1, 1)) >= n or
            CountXOnLine(field, position, (1, 0)) >= n or
            CountXOnLine(field, position, (1, -1)) >= n or
            CountXOnLine(field, position, (0, 1)) >= n)



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

def CountXOnLine(field, position, diff):
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
    

def Hantei(field, pisition, char):
    count, countA

    row = position[0]
    col = position[1]

    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != char or count == 4:
            break

        row += diff[0]
        col += diff[1]
        count += 1
        countA += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]

    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != char or count == 4:
            break

        row -= diff[0]
        col -= diff[1]
        count += 1

    # 阻止か攻撃かを判定
    if count == 4 and countA == 4:
        # 阻止する
        row = position[0]
        col = position[1]

        for x in range(4):
            row += diff[0]
            col += diff[1]

        return (row, col)

    elif count == 4 and countA == 1:
        # 阻止する
        row = position[0] - diff[0]
        col = position[1] - diff[1]

        for x in range(4):
            row -= diff[0]
            col -= diff[1]

    else:
        # 阻止する必要なし
        return None


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
