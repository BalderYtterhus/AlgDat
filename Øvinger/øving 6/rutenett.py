def f(i:int, j:int) -> int:
    roads = [[0 for _ in range(j + 1)] for _ in range(i + 1)]

    roads[i][j] = 1

    for row in range(i, 0, -1):
        for col in range(j, 0, -1):

            if row == i and col == j:
                continue

            right = 0
            down = 0

            if row < i:
                down = roads[row+1][col]
            if col < j:
                right = roads[row][col+1]

            roads[row][col] = right + down

    return roads[1][1]

print(f(1, 1))