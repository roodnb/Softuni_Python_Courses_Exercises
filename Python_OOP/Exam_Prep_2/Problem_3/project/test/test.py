from typing import Optional

from project.furniture import Furniture

from unittest import TestCase, main


class TestFurniture(TestCase):

    def setUp(self):
        self.f = Furniture("Chair", 10.5, (3, 4, 5), True, None)

    def test_init_with_default_values(self):
        self.assertEqual(self.f.model, "Chair")
        self.assertEqual(self.f.price, 10.5)
        self.assertEqual(self.f.dimensions, (3, 4, 5))
        self.assertTrue(self.f.in_stock)
        self.assertIsNone(self.f.weight)

    def test_init_with_passed_values(self):
        f = Furniture("Chair", 10.5, (3, 4, 5), False, 99)
        self.assertEqual(f.model, "Chair")
        self.assertEqual(f.price, 10.5)
        self.assertEqual(f.dimensions, (3, 4, 5))
        self.assertFalse(f.in_stock)
        self.assertEqual(f.weight, 99)

    def test_instance_attributes(self):
        self.assertIsInstance(self.f.model, str)
        self.assertIsInstance(self.f.price, float)
        self.assertIsInstance(self.f.dimensions, tuple)
        self.assertIsInstance(self.f.in_stock, bool)
        self.assertIsInstance(self.f.weight, Optional[float])

    def test_model_non_empty_string_len_more_then_50_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.model = "            "
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(ValueError) as ex:
            self.f.model = ""
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(ValueError) as ex:
            self.f.model = "q" * 51
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_price_value_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.price = -9.
        self.assertEqual(str(ex.exception), "Price must be a non-negative number.")

    def test_dimensions_not_3_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (1, 2)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain 3 integers.")

        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (1, 2, 5, 6)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions_any_zero_or_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (0, 1, 2)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain integers greater than zero.")

        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (-5, 1, 2)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_weight_is_zero_or_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.weight = 0.0
        self.assertEqual(str(ex.exception), "Weight must be greater than zero.")

        with self.assertRaises(ValueError) as ex:
            self.f.weight = -1
        self.assertEqual(str(ex.exception),"Weight must be greater than zero.")

    def test_get_available_status_returns(self):
        result1 = self.f.get_available_status()
        expected1 = f"Model: {self.f._model} is currently {'in stock'}."
        self.assertEqual(result1, expected1)

        self.f.in_stock = False

        result2 = self.f.get_available_status()
        expected2 = f"Model: {self.f._model} is currently {'unavailable'}."
        self.assertEqual(result2, expected2)

    def test_get_specifications(self):
        result1 = self.f.get_specifications()
        expected1 = (f"Model: {self.f.model} has the following dimensions: "
                     f"3mm x 4mm x 5mm and weighs: N/A")
        self.assertEqual(result1, expected1)

        self.f.weight = 99
        result2 = self.f.get_specifications()
        expected2 = (f"Model: {self.f.model} has the following dimensions: "
                     f"3mm x 4mm x 5mm and weighs: 99")
        self.assertEqual(result2, expected2)


if __name__ == "__main__":
    main()

