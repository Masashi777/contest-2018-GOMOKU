#!/usr/bin/python3

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))
    best_position = (0, 0)
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if field[i][j] != '.':
                continue

            # ポジション設定
            position = (i, j)

            # ごれんちゃんが完成するかを判定、そうでなかったら中心に近いところにおく
            # Assume to put a stone on (i, j).
            field[i][j] = 'O'

            if CanHaveFiveStones(field, position, 5):
                DebugPrint('I have a winning choice at (%d, %d)' % (i, j))

                DebugPrint('tag A', i, j)
                field[i][j] = '.'
                return position
            else:
                field[i][j] = '.'
                continue


    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if field[i][j] != '.':
                continue


            # ポジション設定
            position = (i, j)

            field[i][j] = 'X'
            if CanHaveFiveEnemyStones(field, position, 5):
                # すでに４つ並んでる場合
                DebugPrint('tag B', i, j)
                field[i][j] = '.'
                return position
            else:
                field[i][j] = '.'

    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if field[i][j] != '.':
                continue

            # ポジション設定
            position = (i, j)

            # 相手の状態を判定
            field[i][j]='X'
            if CanHaveFiveEnemyStones(field, position, 4):
                # 3つ並んでる場合
                DebugPrint('tag C', i, j)
                field[i][j] = '.'

                # # -----
                # hanteiList = []
                # hanteiList = getHantei(field, position)
                # DebugPrint('Listhantei', hanteiList)
                # for x in hanteiList:
                #     if x != None:
                #         return x
                #         break
                # # -----
                return position
            # elif CanHaveFiveEnemyStones(field, position, 3):
            #     # 2つ並んでる場合
            #     # field[i][j]='O'
            #     DebugPrint('tag H', i, j)
            #     field[i][j] = '.'
            #     return position

            else:
                field[i][j] = '.'

    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if field[i][j] != '.':
                continue

            # ポジション設定
            position = (i, j)

            # 自分の攻撃
            # Assume to put a stone on (i, j).
            field[i][j] = 'O'
            if CanHaveFiveStones(field, position,4):
                DebugPrint('tag D', i, j)
                field[i][j] = '.'
                return position
            elif CanHaveFiveStones(field, position,3):
                # 3つ揃いそうなとき
                DebugPrint('tag E', i, j)
                hanteiList = getHantei(field, position)
                DebugPrint(hanteiList)
                if True in hanteiList and hanteiList.index(True) >= 1:
                    field[i][j] = '.'
                    return position
                else:
                    field[i][j] = '.'
                    continue
            #if CanHaveFiveStones(field, position,2):
            #    return position
            else:
                field[i][j] = '.'
                DebugPrint('tag F', i, j)
                continue

    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if field[i][j] != '.':
                continue

            # ポジション設定
            position = (i, j)

            # Revert the assumption.
            field[i][j] = '.'
            if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                best_position = position
                DebugPrint('tag G', i, j)
    return best_position


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position, num):
    return (CountStonesOnLine(field, position, (1, 1), "O") >= num or
            CountStonesOnLine(field, position, (1, 0), "O") >= num or
            CountStonesOnLine(field, position, (1, -1), "O") >= num or
            CountStonesOnLine(field, position, (0, 1), "O") >= num)

def CanHaveFiveEnemyStones(field, position, n):
    return (CountStonesOnLine(field, position, (1, 1), 'X') >= n or
            CountStonesOnLine(field, position, (1, 0), 'X') >= n or
            CountStonesOnLine(field, position, (1, -1), 'X') >= n or
            CountStonesOnLine(field, position, (0, 1), 'X') >= n)

def getHantei(field, position):
    hanteiList = []

    hanteiList.append(Hantei(field, position, (1, 1), 'O'))
    hanteiList.append(Hantei(field, position, (1, 0), 'O'))
    hanteiList.append(Hantei(field, position, (1, -1), 'O'))
    hanteiList.append(Hantei(field, position, (0, 1), 'O'))

    return hanteiList


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

def Hantei(field, position, diff, mark):
    count = 0
    countA = 0

    row = position[0]
    col = position[1]

    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != mark or count == 3:
            break

        row += diff[0]
        col += diff[1]
        count += 1
        countA += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]

    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != mark or count == 3:
            break

        row -= diff[0]
        col -= diff[1]
        count += 1

    # 阻止か攻撃かを判定
    if count == 3 and countA == 3:
        # 阻止する
        row = position[0]
        col = position[1]

        for x in range(3):
            row += diff[0]
            col += diff[1]

        if row < 0 or col < 0 or row >= N or col >= N:
            return False
        else:
            if field[row][col] == 'X':
                return False
            else:
                return True

    elif count == 3 and countA == 1:
        # 阻止する
        row = position[0]
        col = position[1]

        for x in range(3):
            row -= diff[0]
            col -= diff[1]

        if row < 0 or col < 0 or row >= N or col >= N:
            return False
        else:
            if field[row][col] == 'X':
                return False
            else:
                return True

    else:
        # 阻止する必要なし
        return False


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
