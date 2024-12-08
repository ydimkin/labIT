def triangle(height: int) -> None:
    triangle = [[1]]

    for i in range(1, height):
        row = [1]  
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  
        triangle.append(row)

    for row in triangle:
        print(' '.join(map(str, row)))


def spiral_matrix(n):

    matrix = [[0] * n for _ in range(n)]
    
    num = 1
    left, right = 0, n - 1
    top, bottom = 0, n - 1

    while left <= right and top <= bottom:

        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    for row in matrix:
        print(' '.join(map(str, row)))
    
