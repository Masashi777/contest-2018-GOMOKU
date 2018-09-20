#!/usr/bin/python3

N = 15

TURN_COUNT = 0

# turnCOUNT = 0

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):

    # 変数
    line2, line3, line4, line5
    global TURN_COUNT

    CENTER = (int(N / 2), int(N / 2))

    # ターン数
    TURN_COUNT += 1
    DebugPrint(TURN_COUNT)

    best_position = (0, 0)

    # 5つ揃うかを判定
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

    # 場面の状況把握
    enemyList = getLines(field)

    for x in range(len(enemyList)):
        if len(enemyList[x]) == 2:
            line2.append(enemyList[x])
        elif len(enemyList[x]) == 3:
            line3.append(enemyList[x])
        elif len(enemyList[x]) == 4:
            line4.append(enemyList[x])
        elif len(enemyList[x]) == 5:
            line5.append(enemyList[x])

    # 守りか攻撃の選択
    if len(line3) >= 1 or len(line4) >= 1:
        # 守り
        if len(line4) >= 1:
            # 4つを阻止
        else:
            # 3つを阻止

    else:
        # 攻撃

        for i in range(N):
            for j in range(N):
                if field[i][j] != '.':
                    continue

                # Revert the assumption.
                field[i][j] = '.'
                if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                    best_position = position

                for n in reversed(range(5)):
                    if CanHaveStones(field, position, n):
                        best_position = position


        return best_position

    # if field[i][j] == 'X'

# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
            CountStonesOnLine(field, position, (1, 0)) >= 5 or
            CountStonesOnLine(field, position, (1, -1)) >= 5 or
            CountStonesOnLine(field, position, (0, 1)) >= 5)

# TODO ORIGINAL
def CanHaveStones(field, position, num):
    return (CountStonesOnLine(field, position, (1, 1)) == num or
            CountStonesOnLine(field, position, (1, 0)) == num or
            CountStonesOnLine(field, position, (1, -1)) == num or
            CountStonesOnLine(field, position, (0, 1)) == num)


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

# GET LINES
def getLines(field):

    checkList = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    enemyList

    for i in range(N):
        for j in range(N):
            # ポジションの設定
            row = i
            col = j

            # x軸のチェック
            listA
            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listA.append((i, j))
                row += checkList[0][0]
                col += checkList[0][1]

            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listA.append((i, j))
                row += checkList[1][0]
                col += checkList[1][1]

            if len(listA) >= 2 and listA not in enemyList:
                enemyList.append(listA)

            # y軸のチェック
            listB
            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listB.append((i, j))
                row += checkList[2][0]
                col += checkList[2][1]

            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listB.append((i, j))
                row += checkList[3][0]
                col += checkList[3][1]

            if len(listB) >= 2 and listB not in enemyList:
                enemyList.append(listB)

            # x=y軸のチェック
            listC
            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listA.append((i, j))
                row += checkList[4][0]
                col += checkList[4][1]

            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listA.append((i, j))
                row += checkList[5][0]
                col += checkList[5][1]

            if len(listC) >= 2 and listC not in enemyList:
                enemyList.append(listC)

            # x=-y軸のチェック
            listD
            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listA.append((i, j))
                row += checkList[6][0]
                col += checkList[6][1]

            while True:
                if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
                    break

                listA.append((i, j))
                row += checkList[7][0]
                col += checkList[7][1]

            if len(listD) >= 2 and listD not is enemyList:
                enemyList.append(listD)

    DebugPrint(enemyList)
    return enemyList

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
