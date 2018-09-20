#!/usr/bin/python3

N = 15
direction_list = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]
patternA = ['.OOOOX', float("inf")]
patternB = ['XOOOO.', 4]
patternE = ['.OOO.', 2]
patternE_ = ['.OOO.O', 2]
patternF = ['XOOO.', 1]
patternF_ = ['XOOO.OX', 1]
patternF__ = ['XOOO.O', 1]
patterns = [patternA, patternB, patternE,
            patternF]


# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.


# def Think(field):
#     (place, point) = Solve(field)
#     field[place[0]][place[1]] = 'O'
#     for i in range(N):
#         for j in range(N):
#             if field[i][j] == 'O':
#                 field[i][j] = 'X'
#             elif field[i][j] == 'X':
#                 field[i][j] = 'O'

#     (place_, point_) = Solve(field)
#     if point_ == float('inf')


def Think(field):
    large_field = [['X' for i in range(17)] for j in range(17)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):

            large_field[i][j] = field[i - 1][j - 1]

    best_position = (0, 0)
    max_point = - 1
    max_place = (0, 0)
    for i in range(N):
        for j in range(N):
            i = (i + N // 2) % N
            j = (j + N // 2) % N
            sum_score = 0
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

            for direction in direction_list:
                for pat in patterns:
                    for place_idx in range(len(pat[0])):
                        place = (i - direction[0] * place_idx + 1,
                                 j - direction[1] * place_idx + 1)
                        sum_score += MatchLinePoint(large_field, place,
                                                    direction, pat[0], pat[1])
            if sum_score > max_point:
                max_point = sum_score
                max_place = (i, j)
                # if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                #    best_position = position
    best_position = max_place

    return best_position


# Returns true if you have five stones from |position|. Returns false
# otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
            CountStonesOnLine(field, position, (1, 0)) >= 5 or
            CountStonesOnLine(field, position, (1, -1)) >= 5 or
            CountStonesOnLine(field, position, (0, 1)) >= 5)


# Returns the number of stones you can put around |position| in the
# direction specified by |diff|.
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


def MatchLinePoint(field, position, diff, pattern, score):
    count = 0

    row = position[0]
    col = position[1]
    for i in range(len(pattern)):
        if row < 0 or col < 0 or row >= 17 or col >= 17 or field[row][col] != pattern[i]:
            return 0
        row += diff[0]
        col += diff[1]

    return score

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

