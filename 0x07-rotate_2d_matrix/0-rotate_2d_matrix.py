def rotate_2d_matrix(matrix):
  """rotates a 2d matrix 90° clockwise
  Returns: Nothing"""
  # Make a copy of the matrix.
  new_matrix = matrix[:]

  left, right = 0, len(matrix) - 1

  while left < right:
    for i in range(right - left):
      top, bottom = left, right
      topLeft = new_matrix[top][left + i]
      new_matrix[top][left + i] = new_matrix[bottom - i][left]
      new_matrix[bottom - i][left] = new_matrix[bottom][right - i]
      new_matrix[bottom][right - i] = new_matrix[top + i][right]
      new_matrix[top + i][right] = topLeft
    right -= 1
    left += 1
