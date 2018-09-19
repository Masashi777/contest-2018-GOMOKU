#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))

    best_position = (0, 0)
    olist = []
    xlist = []
    forlist = []
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue
                # if i > 0 and j > 0 and i < N - 1 and j < N - 1:
                #     DebugPrint(field[i][j])
                #     DebugPrint('segfo (%d, %d)' % (i, j))
                #     if field[i][j] == 'O':
                #         left = False
                #         right = False
                #         up = False
                #         down = False
                #         if field[i][j-1] == 'O':
                #             left = True
                #         if field[i][j+1] == 'O':
                #             right = True
                #         if field[i+1][j] == 'O':
                #             up = True
                #         if field[i-1][j] == 'O':
                #             down = True
                #         if left and up:
                #             if field[i-1][j-1] == '.':
                #                 forlist.append((i-1, j-1))
                #         if left and down:
                #             if field[i+1][j-1] == '.':
                #                 forlist.append((i+1, j-1))
                #         if right and up:
                #             if field[i-1][j+1] == '.':
                #                 forlist.append((i-1, j+1))
                #         if right and down:
                #             if field[i+1][j+1] == '.':
                #                 forlist.append((i+1, j+1))


            position = (i, j)
            # Assume to put a stone on (i, j).
            field[i][j] = 'O'
            mark = 'O'
            if CanHaveNumStones(field, position, mark, 5):
                DebugPrint('I have a winning choice at (%d, %d)' % (i, j))
                return position

            # Assume aite 3
            field[i][j] = 'X'
            mark = 'X'
            if CanHaveNumStones(field, position, mark, 5):
                xlist.append((i,j))
                return position 

            mark = 'O'
            if CanHaveNumStones(field, position, mark, 4):
                olist.append((i,j))

            mark = 'X'
            # どっちがいいか
            if CanHaveNumStones(field, position, mark, 4):
                xlist.append((i,j))

            # Revert the assumption.
            field[i][j] = '.'
            if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                best_position = position


    if olist != []:
        DebugPrint('olist')
        best_position = olist[0]
        if len(olist) > 1:
            for ol in olist:
                position = ol
                if GetDistance(best_position, CENTER)  > GetDistance(position, CENTER):
                    best_position = ol

    if xlist != []:
        DebugPrint('xlist')
        best_position = xlist[0]
        if len(xlist) > 1:
            for xl in xlist:
                position = xl
                if GetDistance(best_position, CENTER)  > GetDistance(position, CENTER):
                    best_position = xl




    if forlist != []:
        DebugPrint('forlist')
        best_position = forlist[0]
        for fl in forlist:
            position = fl
            if GetDistance(best_position, CENTER)  > GetDistance(position, CENTER):
                best_position = fl


    return best_position


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveNumStones(field, position, mark, score):

    return (CountStonesOnLine(field, position, (1, 1), mark) >= score or
            CountStonesOnLine(field, position, (1, 0), mark) >= score or
            CountStonesOnLine(field, position, (1, -1), mark) >= score or
            CountStonesOnLine(field, position, (0, 1), mark) >= score)
   


# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountStonesOnLine(field, position, diff, mark):
    count = 0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != mark:
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != mark:
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

