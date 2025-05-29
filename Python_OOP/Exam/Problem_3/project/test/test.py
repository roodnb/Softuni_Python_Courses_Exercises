from project.volcano import Volcano
from unittest import TestCase, main


class TestVolcano(TestCase):

    def test_init_with_default_values(self):
        v = Volcano("Jordan", 1000, None)
        self.assertEqual(v.name, "JORDAN")
        self.assertEqual(v.height_m, 1000)
        self.assertIsNone(v.last_eruption)

    def test_init_with_passed_values(self):
        v = Volcano("Antonov", 1000, 350)
        self.assertEqual(v.name, "ANTONOV")
        self.assertEqual(v.height_m, 1000)
        self.assertEqual(v.last_eruption, 350)

    def test_instance_attributes(self):
        v = Volcano("Peter", 1000, 350)
        self.assertIsInstance(v.name, str)
        self.assertIsInstance(v.height_m, int)
        self.assertIsInstance(v.last_eruption, int)

    def test_name_len_below_2_raises(self):
        v = Volcano("Genadi", 1000, None)
        with self.assertRaises(ValueError)as ex:
            v.name = "a"
        self.assertEqual(str(ex.exception), "Volcano name must be at least two characters long!")

    def test_name_in_unique_names_raises(self):
        v = Volcano("Alabala", 1000, None)
        with self.assertRaises(ValueError) as ex:
            p = Volcano("Jordan", 1000, None)
        self.assertEqual(str(ex.exception), "Volcano name must be unique!")

    def test_height_m_zero_or_negative_raises(self):
        v = Volcano("Ebahgo", 1000, None)
        with self.assertRaises(ValueError) as ex:
            v.height_m = 0
        self.assertEqual(str(ex.exception), "Height must be a positive integer!")

        with self.assertRaises(ValueError) as ex:
            v.height_m = -1
        self.assertEqual(str(ex.exception), "Height must be a positive integer!")

    def test_is_active_is_False(self):
        v = Volcano("mnzle", 1000, None)
        self.assertFalse(v.is_active)

    def test_is_active_is_true(self):
        v = Volcano("da bqhte kazali kak se testtvat class atributi", 1000, None)
        v.last_eruption = 2000
        self.assertTrue(v.is_active)

    def test_unique_volcano_count(self):
        v = Volcano("maika vi nasrana", 1000, None)
        self.assertEqual(len(v._unique_names), 9)

if __name__ == "__main__":
    main()