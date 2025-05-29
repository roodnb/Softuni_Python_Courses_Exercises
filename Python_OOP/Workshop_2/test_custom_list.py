from Custom_List.custom_list import CustomList
from unittest import TestCase, main


class CustomListTests(TestCase):
    def setUp(self):
        self.c = CustomList(1, 2, 3)

    def test_init(self):
        self.assertEqual(self.c._CustomList__value, [1, 2, 3])

    def test_append(self):
        result = self.c.append(5)

        self.assertEqual(self.c._CustomList__value, [1, 2, 3, 5])
        self.assertEqual(result, [1, 2, 3, 5])

    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.c.remove(-1)
        self.assertEqual(str(ex.exception), "Invalid index")
        self.assertEqual(self.c._CustomList__value, [1, 2, 3])

        with self.assertRaises(IndexError) as ex:
            self.c.remove(len(self.c._CustomList__value))
        self.assertEqual(str(ex.exception), "Invalid index")
        self.assertEqual(self.c._CustomList__value, [1, 2, 3])

    def test_remove(self):
        self.assertEqual(self.c._CustomList__value, [1, 2, 3])

        result = self.c.remove(2)

        self.assertEqual(self.c._CustomList__value, [1, 2])
        self.assertEqual(result, 3)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.c.get(-1)
        self.assertEqual(str(ex.exception), "Invalid index")

        with self.assertRaises(IndexError) as ex:
            self.c.get(len(self.c._CustomList__value))
        self.assertEqual(str(ex.exception), "Invalid index")

    def tests_get(self):
        result = self.c.get(2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    main()