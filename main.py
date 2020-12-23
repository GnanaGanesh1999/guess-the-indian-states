def cntRect(mat, m,
            l, b):

    end_points = [[0, 0], [l, 0], [0, b], [l, b]]
    horizontal_count = set([])
    vertical_count = set([])
    horizontal_count.add(0)
    vertical_count.add(0)
    horizontal_count.add(end_points[3][0])
    vertical_count.add(end_points[3][1])
    for i in range(N):
        horizontal_count.add(mat[i][0])
        vertical_count.add(mat[i][1])

    return ((len(horizontal_count) - 1) *
            (len(vertical_count) - 1))


end_points = [[0, 0], [0, 5],
              [5, 0], [5, 5]]
points = [[1, 2], [3, 4]]
N = len(points)
print(cntRect(points, N, 5, 5))
