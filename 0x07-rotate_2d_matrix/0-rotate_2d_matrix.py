def rotate_2d_matrix(matrix):
  n = len(matrix)
  for layer in range(n // 2):
    first = layer
    last = n - layer - 1
    for i in range(last - first):
      # Swap the elements in the current layer.
      matrix[first][first + i], matrix[last - i][last], matrix[last][first + i], matrix[first][last - i] = \
        matrix[last][first + i], matrix[first][last - i], matrix[first][first + i], matrix[last - i][last]


if __name__ == "__main__":
  matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

  rotate_2d_matrix(matrix)
  print(matrix)
