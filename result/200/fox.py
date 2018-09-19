#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))
    # initial
    if ifStart(field) == True:
        return CENTER
    
    # other
    best_score = 0
    best_position = (-1, -1)
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':  # if O, X
                continue

            position = (i, j)
            if best_position == (-1, -1):
                best_position = position

            # Assume to put a stone on (i, j).
            field[i][j] = 'O'
            if CanHaveFiveStones(field, position):
                # DebugPrint('I have a winning choice at (%d, %d)' % (i, j))
                return position

            score = scoring(field)
            # DebugPrint(score)

            # Revert the assumption.
            field[i][j] = '.'
            if score > best_score:
                best_position = position
                best_score = score
            # if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
            #     best_position = position
    DebugPrint("score = ", best_score)
    return best_position

def ifStart(field):
    count = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                return False
    return True


def scoring(field):
    # 4 no side (victory 9999)
    # 3 no side (300)
    # 2 no side (200)
    num4 = CanHaveNStones(field, 4, 'O')
    num3 = CanHaveNStones(field, 3, 'O')
    num2 = CanHaveNStones(field, 2, 'O')
    # DebugPrint(num2, num3, num4)

    return num4*99999 + num3*300 + num2*200 #- 0.2*best_score

# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1), 'O') >= 5 or
            CountStonesOnLine(field, position, (1, 0), 'O') >= 5 or
            CountStonesOnLine(field, position, (1, -1), 'O') >= 5 or
            CountStonesOnLine(field, position, (0, 1), 'O') >= 5)

# Returns position if you have 3 stones from |position|. Returns false otherwise.
def CanHaveNStones(field, n, s):
    count = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] == s:
                position = (i, j)
                for d in [(1, 1), (1, 0), (1, -1), (0, 1)]:
                    row = i-d[0]
                    col = j-d[1]
                    if not (row < 0 or col < 0 or row >= N or col >= N):                        
                        if (CountStonesOnLine(field, position, d, s) == n and 
                            field[row][col] == '.'):
                            count += 0.5
                                        

                    row = i+n*d[0]
                    col = j+n*d[1]

                    if not (row < 0 or col < 0 or row >= N or col >= N):                        
                        if (CountStonesOnLine(field, position, d, s) == n and 
                            field[row][col] == '.'):
                            count += 0.5   

    # DebugPrint("count = ", count)
    return count



# Returns true if enermy have 3 stones from |position|. Returns false otherwise.
def CanEnermyHaveNStones(field, position, n):
    return (CountStonesOnLine(field, position, (1, 1), 'X') >= n or
            CountStonesOnLine(field, position, (1, 0), 'X') >= n or
            CountStonesOnLine(field, position, (1, -1), 'X') >= n or
            CountStonesOnLine(field, position, (0, 1), 'X') >= n)

# 相手が３つ並べしたら隣に置く

# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountStonesOnLine(field, position, diff, s):
    count = 0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != s:
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != s:
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

