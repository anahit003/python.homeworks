class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for col in range(cols)] for row in range(rows)]

    def __str__(self):
        string = ""
        for row in range(self.rows):
            for col in range(self.cols):
                string += str(self.matrix[row][col]) + " "
            string += "\n"
        return string

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("matrices must be the same size ")

        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be the same size ")

        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.matrix[row][col] = self.matrix[row][col] - other.matrix[row][col]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("number of columns in the first matrix must equal the number of rows in the second matrix to multiply.")

        result = Matrix(self.rows, other.cols)
        for row in range(self.rows):
            for col in range(other.cols):
                for i in range(self.cols):
                    result.matrix[row][col] += self.matrix[row][i] * other.matrix[i][col]
        return result


m1 = Matrix(2,2)
m1.matrix = [[1, 9], [4, 4]]

m2 = Matrix(2, 2)
m2.matrix = [[6, 3], [4, 5]]

print(m1)
print(m2)

print(m1 + m2)
print(m1 - m2)
print(m1 * m2)
