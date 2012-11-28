from matrix import Matrix, Foo
import unittest

class TestMatrixFunction(unittest.TestCase):

    matrix_1 = Matrix([[5, 1, 1], [1, 4, 1]])
    matrix_2 = Matrix([[2, 2, 5], [3, 5, 3]])
    test_matrix = matrix_2

    def test_correct_result(self):
        self.matrix_3 = self.matrix_1 + self.matrix_2
        self.assertEqual([[7, 3, 6], [4, 9, 4]], self.matrix_3)

    def test_proportional_matrix(self):
        self.assertEqual(self.matrix_1.get_cols(), self.matrix_2.get_cols())
        self.assertEqual(self.matrix_1.get_rows(), self.matrix_2.get_rows())

    def test_get_rows_and_cols(self):
        self.assertEqual(self.matrix_1.get_rows(), 2)
        self.assertEqual(self.matrix_1.get_cols(), 3)

class TestFooFunction(unittest.TestCase):

    test_matrix_foo = Foo
    test_matrix_foo_1 = Foo
    test_matrix_foo_2 = Foo
    test_matrix_foo_3 = Foo
    test_matrix_foo_1 = test_matrix_foo.bar(test_matrix_foo, [[1], [2], [3], [4]])
    test_matrix_foo_3 = test_matrix_foo_2.baz(test_matrix_foo)

    def test_method_bar(self):
       pass
