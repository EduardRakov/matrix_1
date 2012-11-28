class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, matrix):
        if self.get_rows() == matrix.get_rows() and self.get_cols() == matrix.get_cols():
            result = [0] * self.get_rows()

            for row in range(self.get_rows()):
                result[row] = [0] * self.get_cols()
                for col in range(self.get_cols()):
                    result[row][col] = self.matrix[row][col] + matrix[row][col]

            return result
        else:
            raise Exception('Matrices are not proportional')

    def get_cols(self):
        return len(self.matrix[0])

    def get_rows(self):
        return len(self.matrix)


class Foo():

    global weight
    weight = [0] * 4
    for i in range(4):
        weight[i] = [0] * 4

    def bar(self, vector):
        matrix_2 = list(vector)
        matrix_1 = list(zip(*matrix_2))
        identity = [0] * len(matrix_2)
        matrix_3 = [0] * len(matrix_2)
        matrix_4 = [0] * len(matrix_2)

        for i in range(len(matrix_2)):
            identity[i] = [0] * len(matrix_3)
            identity[i][i] = 1
            matrix_3[i] = [0] * len(matrix_2)
            matrix_4[i] = [0] * len(matrix_2)
            for j in range(len(matrix_2)):
                matrix_3[i][j] = matrix_1[0][j] * matrix_2[i][0]
                matrix_4[i][j] = matrix_3[i][j] - identity[i][j]
                weight[i][j] = weight[i][j] + matrix_4[i][j]

    def baz(self, vector):
        inputMatrix = list(vector)
        columnMatrix_1 = [0] * len(inputMatrix)
        result_vector = list()
        for k in range(len(weight)):
            for i in range(k+1, len(weight)):
                result = 0
                for j in range(len(weight)):
                    result += weight[k][j] * weight[i][j]
                if result > 0:
                        result_vector.append(result)
        print("result_1", result)
        print("result_vector", result_vector)
        print("columnMatrix_1", weight)
        return result_vector