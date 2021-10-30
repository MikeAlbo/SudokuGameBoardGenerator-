# Sudoku game board generator

a Python 3 console app that generates a list of Sudoku Game Boards.

## to run
1. `cd <project dir>`
2. run: `Python3 gameboards.py`
3. follow prompted instructions

## JSON structure
```json
[
  {
    "board_id": 1,
    "game_board": [[9, 6, 7, 5, 3, 8, 2, 4, 1], [1, 4, 2, 9, 7, 6, 3, 8, 5], [5, 8, 3, 1, 2, 4, 7, 6, 9], [8, 3, 1, 4, 9, 2, 5, 7, 6], [6, 7, 5, 8, 1, 3, 9, 2, 4], [4, 2, 9, 6, 5, 7, 1, 3, 8], [2, 9, 6, 7, 8, 5, 4, 1, 3], [3, 1, 4, 2, 6, 9, 8, 5, 7], [7, 5, 8, 3, 4, 1, 6, 9, 2]]
  },
  {
    "board_id": 2, 
    "game_board": [[8, 7, 6, 3, 9, 4, 2, 1, 5], [4, 3, 9, 5, 2, 1, 6, 8, 7], [1, 5, 2, 7, 6, 8, 9, 4, 3], [2, 1, 7, 8, 3, 6, 5, 9, 4], [9, 4, 5, 1, 7, 2, 3, 6, 8], [6, 8, 3, 4, 5, 9, 7, 2, 1], [7, 2, 8, 6, 4, 3, 1, 5, 9], [3, 6, 4, 9, 1, 5, 8, 7, 2], [5, 9, 1, 2, 8, 7, 4, 3, 6]]
  }
]
```
