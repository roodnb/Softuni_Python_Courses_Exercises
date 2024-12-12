# Practice 2 Test case - full capacity
from unittest import TestCase, main


class TestBoardingPassengers(TestCase):
    def test_boarding_passengers(self):
        result = boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold'))
        expected = """Boarding details by benefit plan:
## Diamond: 35 guests
## First Cruiser: 25 guests
## Gold: 25 guests
## Platinum: 15 guests
Boarding unsuccessful. Cruise ship at full capacity."""
        self.assertEqual(result.strip(), expected)


if __name__ == '__main__':
    main()