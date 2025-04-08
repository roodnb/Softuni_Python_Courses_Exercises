from project.vehicle import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.v = Vehicle(125.0, 200.0)

    def test_init(self):
        self.assertEqual(self.v.fuel, 125.0)
        self.assertEqual(self.v.horse_power, 200.0)
        self.assertEqual(self.v.capacity, 125.0)
        self.assertEqual(self.v.fuel_consumption, 1.25)

    def test_class_attributes_type(self):
        self.assertIsInstance(self.v.fuel, float)
        self.assertIsInstance(self.v.fuel_consumption, float)
        self.assertIsInstance(self.v.capacity, float)
        self.assertIsInstance(self.v.horse_power, float)

    def test_drive_not_enough_fuel_raises(self):
        self.assertEqual(self.v.fuel, 125)
        with self.assertRaises(Exception) as ex:
            self.v.drive(125)
        self.assertEqual(str(ex.exception), "Not enough fuel")
        self.assertEqual(self.v.fuel, 125)

    def test_drive(self):
        self.assertEqual(self.v.fuel, 125)
        self.v.drive(100)
        self.assertEqual(self.v.fuel, 0)

        self.v.fuel = 125
        self.v.drive(60)
        self.assertEqual(self.v.fuel, 50)

    def test_refuel_more_capacity_raises(self):
        self.assertEqual(self.v.fuel, 125)
        self.v.drive(60)
        self.assertEqual(self.v.fuel, 50)

        with self.assertRaises(Exception) as ex:
            self.v.refuel(100)

        self.assertEqual(str(ex.exception), "Too much fuel")
        self.assertEqual(self.v.fuel, 50)

    def test_refuel(self):
        self.assertEqual(self.v.fuel, 125)
        self.v.drive(60)
        self.assertEqual(self.v.fuel, 50)
        self.v.refuel(75)
        self.assertEqual(self.v.fuel, 125)

    def test_str(self):
        result = self.v.__str__()
        expecter_result = f"The vehicle has {self.v.horse_power} " \
               f"horse power with {self.v.fuel} fuel left and {self.v.fuel_consumption} fuel consumption"
        self.assertEqual(result, expecter_result)


if __name__ == "__main__":
    main()

