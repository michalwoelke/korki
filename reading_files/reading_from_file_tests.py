import unittest
import reading_from_file


class MyTestCase(unittest.TestCase):
    def test_read_string(self):
        expected = "This is some string example,\nnothing special, but should be read\nas it is."
        actual = reading_from_file.read_string('test_inputs/string.txt')
        self.assertEqual(expected, actual)

    def test_space_list(self):
        expected = ["one", "two", "three", "four", "five", "six", "seven", "eight", "23"]
        actual = reading_from_file.read_space_list('test_inputs/space-list.txt')
        self.assertEqual(expected, actual)

    def test_read_list(self):
        expected = [1234, 1235, 1236, 12346]
        actual = reading_from_file.read_list('test_inputs/list.txt')
        self.assertEqual(expected, actual)

    def test_read_comma_list(self):
        expected = [23, 4, 2, 123, 1234, -421, 321, 3]
        actual = reading_from_file.read_comma_list('test_inputs/comma-list.txt')
        self.assertEqual(expected, actual)

    def test_read_2d_table(self):
        expected = [
            ['g', 'a', 'l', 'k', 'i', 'j', 'd', 'f', 'a', 'o', 'i'],
            ['a', 'g', 'e', 'o', 'r', 'i', 'u', 'h', 'j', 'o', 'i'],
            ['p', 'o', 'a', 'k', 'g', 'p', 'w', 'e', 'w', 'f', 'a'],
            ['o', 'e', 'g', 'h', 'n', 'a', 'r', 'i', 'j', 'w', 'g'],
        ]
        actual = reading_from_file.read_2d_table('test_inputs/list_2d.txt')
        self.assertEqual(expected, actual)

    def test_read_2d_int_table(self):
        expected = [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [1, 3, 2, 4, 1],
            [3, 2, 3, 1, 4],
            [1, 2, 3, 4, 3]
        ]
        actual = reading_from_file.read_2d_int_table('test_inputs/int_list_2d.txt')
        self.assertEqual(expected, actual)

    def test_read_curly_wrapped_list(self):
        expected = [123, 3241, 32314, 32431, 32, 4123, 4, 31234, 3212]
        actual = reading_from_file.read_curly_wrapped_list('test_inputs/curly_wrapped_list.txt')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
