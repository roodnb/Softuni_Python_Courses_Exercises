from car_manager import Car

from unittest import TestCase, main


class CarTests(TestCase):

    def test_init(self):
        c = Car("Skoda", "Octavia", 10, 55)
        self.assertEqual(c.make, "Skoda")
        self.assertEqual(c.model, "Octavia")
        self.assertEqual(c.fuel_consumption, 10)
        self.assertEqual(c.fuel_capacity, 55)
        self.assertEqual(c.fuel_amount, 0)

    def test_make_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("", "Octavia", 10, 55)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

        with self.assertRaises(Exception) as ex:
            Car(None, "Octavia", 10, 55)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("Skoda", "", 10, 55)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

        with self.assertRaises(Exception) as ex:
            Car("Skoda", None, 10, 55)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("Skoda", "Octavia", 0, 55)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("Skoda", "Octavia", -1, 55)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("Skoda", "Octavia", 10, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("Skoda", "Octavia", 10, -10)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_negative_raises(self):
        c = Car("Skoda", "Octavia", 10, 55)
        self.assertEqual(c.fuel_amount, 0)
        with self.assertRaises(Exception) as ex:
            c.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

        self.assertEqual(c.fuel_amount, 0)

    def test_refuel_fuel_zero_or_negative_raises(self):
        c = Car("Skoda", "Octavia", 10, 55)
        self.assertEqual(c.fuel_amount, 0)
        with self.assertRaises(Exception) as ex:
            c.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            c.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_fuel_greater_then_zero(self):
        c = Car("Skoda", "Octavia", 10, 55)
        self.assertEqual(c.fuel_amount, 0)
        c.refuel(10)
        self.assertEqual(c.fuel_amount, 10)
        c.refuel(10)
        self.assertEqual(c.fuel_amount, 20)

        c.refuel(50)
        self.assertEqual(c.fuel_amount, 55)

    def test_drive_not_enough_fuel_raises(self):
        c = Car("Skoda", "Octavia", 10, 55)
        c.refuel(c.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            c.drive(800)

        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")
        self.assertEqual(c.fuel_capacity, c.fuel_amount)

    def test_drive(self):
        c = Car("Skoda", "Octavia", 10, 55)
        c.refuel(c.fuel_capacity)

        c.drive(550)
        self.assertEqual(0 , c.fuel_amount)

        c.refuel(c.fuel_capacity)
        self.assertEqual(55, c.fuel_amount)
        c.drive(300)
        self.assertEqual(25, c.fuel_amount)


if __name__ == "__main__":
    main()