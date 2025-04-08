from extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1,3,4,-1,100)

    def test_init_stores_only_ints(self):
        # No args
        l = IntegerList()

        self.assertEqual(l._IntegerList__data, [])

        l = IntegerList(1, 'str', 9.5, -1, {1: 1}, ("tralala", 4), [1, 2, 3])
        self.assertEqual(l._IntegerList__data, [1, -1])

    def test_get_data(self):
        result = self.integer_list.get_data()
        expected_result = [1,3,4,-1,100]

        self.assertEqual(expected_result, result)

    def test_add_not_int_raises(self):
        result = self.integer_list.get_data()
        expected_result = [1, 3, 4, -1, 100]
        self.assertEqual(expected_result, result)

        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("123")
        self.assertEqual(str(ex.exception), "Element is not Integer")

        result = self.integer_list.get_data()
        expected_result = [1, 3, 4, -1, 100]
        self.assertEqual(expected_result, result)

    def test_add(self):
        result = self.integer_list.get_data()
        expected_result = [1, 3, 4, -1, 100]
        self.assertEqual(expected_result, result)

        result = self.integer_list.add(5)
        expected_result = [1, 3, 4, -1, 100, 5]
        self.assertEqual(expected_result, result)
        second_result = self.integer_list.get_data()
        self.assertEqual(expected_result, second_result)

    def test_remove_not_index_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 5)
        # index is equal to the len
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(5)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 5)

        # index is greater then len
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(8)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 5)

    def test_remove_index(self):
        self.assertEqual(self.integer_list.get_data()[2], 4)
        self.assertEqual(len(self.integer_list.get_data()), 5)

        result = self.integer_list.remove_index(2)
        self.assertEqual(result, 4)
        self.assertEqual(self.integer_list.get_data()[2], -1)
        self.assertEqual(len(self.integer_list.get_data()), 4)

    def test_get_not_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 5)

        # index is equal to the len
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(5)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 5)

        # index is greater then len
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(8)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 5)

    def test_get(self):
        self.assertEqual(self.integer_list.get_data()[2], 4)
        self.assertEqual(len(self.integer_list.get_data()), 5)
        result = self.integer_list.get(2)
        expected_result = 4
        self.assertEqual(expected_result, result)
        self.assertEqual(len(self.integer_list.get_data()), 5)

    def test_insert_index_invalid_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 5)
        # index is equal to the len
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(5, 27)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 5)
        # index is greater then len
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(5, 27)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 5)

    def test_insert_invalid_el_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 5)

        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(4, "str")
        self.assertEqual(str(ex.exception), "Element is not Integer")

        self.assertEqual(len(self.integer_list.get_data()), 5)

    def test_insert(self):
        self.assertEqual(len(self.integer_list.get_data()), 5)
        self.assertEqual(self.integer_list.get_data()[2], 4)

        self.integer_list.insert(2, 24)
        result = self.integer_list.get_data()[2]
        expected_result = 24
        self.assertEqual(expected_result, result)
        self.assertEqual(len(self.integer_list.get_data()), 6)

    def test_get_biggest(self):
        self.assertEqual(self.integer_list.get_data(), [1,3,4,-1,100])
        result = self.integer_list.get_biggest()
        expected_result = 100
        self.assertEqual(expected_result, result)

        self.integer_list.insert(2, 200)
        result = self.integer_list.get_biggest()
        self.assertEqual(200, result)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_data()[2], 4)
        result = self.integer_list.get_index(4)
        expected_result = 2
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()