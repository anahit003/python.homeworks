class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for i in range(m)] for j in range(n)]

    def print_matrix(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.matrix[i][j], end=" ")
            print()

    def calculate_mean(self):
        mean = 0
        for i in range(self.n):
            for j in range(self.m):
                mean += self.matrix[i][j]
        mean /= self.n * self.m
        return mean

    def calculate_sum_of_row(self, row):
        sum = 0
        for i in range(self.m):
            sum += self.matrix[row][i]
        return sum

    def calculate_average_of_column(self, column):
        average = 0
        for i in range(self.n):
            average += self.matrix[i][column]
        average /= self.n
        return average

    def print_submatrix(self, col1, col2, row1, row2):
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                print(self.matrix[i][j], end=" ")
            print()

def main():
    matrix = Matrix(3, 3)

    matrix.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix.print_matrix()

    
    mean = matrix.calculate_mean()
    print("Mean:", mean)

    sum_of_row = matrix.calculate_sum_of_row(1)
    print("Sum of second row:", sum_of_row)

    average_of_column = matrix.calculate_average_of_column(0)
    print("Average of first column:", average_of_column)

    print("submatrix")
    matrix.print_submatrix(1, 1, 2, 2)

if __name__ == "__main__":
    main()
