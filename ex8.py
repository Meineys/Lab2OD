def print_grid(matrix):
    for row in matrix:
        print("".join(map(str, row)))


def find_empty(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return (i, j)
    return None


def is_valid(matrix, num, pos):
    row, col = pos

    for j in range(4):
        if matrix[row][j] == num and col != j:
            return False

    for i in range(4):
        if matrix[i][col] == num and row != i:
            return False

    box_x = col // 2
    box_y = row // 2
    for i in range(box_y * 2, box_y * 2 + 2):
        for j in range(box_x * 2, box_x * 2 + 2):
            if matrix[i][j] == num and (i, j) != pos:
                return False

    return True


def solve_sudoku(matrix):
    empty = find_empty(matrix)
    if not empty:
        return True

    row, col = empty
    for i in range(1, 5):
        if is_valid(matrix, i, (row, col)):
            matrix[row][col] = i

            if solve_sudoku(matrix):
                return True

            matrix[row][col] = 0

    return False


grid = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

solve_sudoku(grid)
print_grid(grid)