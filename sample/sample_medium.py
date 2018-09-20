#!/usr/bin/python3

import sys

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
  scores = {}
  for i in range(N):
    for j in range(N):
      if field[i][j] != '.':
        continue

      position = (i, j)
      if HaveMultipleStones(field, position, 'O', 5):
        scores[position] = 0
      elif HaveMultipleStones(field, position, 'X', 5):
        scores[position] = 1
      elif HaveMultipleStones(field, position, 'O', 4):
        scores[position] = 2
      elif HaveMultipleStones(field, position, 'X', 4):
        scores[position] = 3
      elif HaveMultipleStones(field, position, 'O', 3):
        scores[position] = 4
      elif HaveMultipleStones(field, position, 'X', 3):
        scores[position] = 5
      elif HaveMultipleStones(field, position, 'O', 2):
        scores[position] = 6
      elif HaveMultipleStones(field, position, 'X', 2):
        scores[position] = 7
      else:
        scores[position] = 8

  sorted_scores = sorted(scores.items(), key=lambda x: x[1])
  return sorted_scores[0][0]

# Returns true if you have a five-stones line from |position|. Returns false otherwise.
def HaveMultipleStones(field, position, stone, count):
  return (CountStonesOnLine(field, position, stone, (1, 1)) >= count or
          CountStonesOnLine(field, position, stone, (1, 0)) >= count or
          CountStonesOnLine(field, position, stone, (1, -1)) >= count or
          CountStonesOnLine(field, position, stone, (0, 1)) >= count)

# Returns the number of stones on the line segment on the direction of |diff| from |position|.
def CountStonesOnLine(field, position, stone, diff):
  count = 1

  row = position[0] + diff[0]
  col = position[1] + diff[1]
  while True:
    if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != stone:
      break
    row += diff[0]
    col += diff[1]
    count += 1

  row = position[0] - diff[0]
  col = position[1] - diff[1]
  while True:
    if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != stone:
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

if __name__  == '__main__':
  main()
