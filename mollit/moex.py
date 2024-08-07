def calculate_next_island_id(matrix):
    def dfs(i, j, matrix):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == '0':
            return
        matrix[i][j] = '0'  # Mark cell as visited
        dfs(i + 1, j, matrix)  # Visit adjacent cells
        dfs(i - 1, j, matrix)
        dfs(i, j + 1, matrix)
        dfs(i, j - 1, matrix)

    island_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                island_count += 1
                dfs(i, j, matrix)

    return island_count + 1  # Return current_island_id + 1
