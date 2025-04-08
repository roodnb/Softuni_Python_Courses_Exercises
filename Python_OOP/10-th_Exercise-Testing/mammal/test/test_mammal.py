from project.mammal import Mammal
from unittest import TestCase, main


class Test_Mammal(TestCase):
    def setUp(self):
        self.m = Mammal("Jordan", "human", "jungle")

    def test_init(self):
        self.assertEqual(self.m.name, "Jordan")
        self.assertEqual(self.m.type, "human")
        self.assertEqual(self.m.sound, "jungle")
        self.assertEqual(self.m._Mammal__kingdom, "animals")

    def test_make_sound(self):
        result = self.m.make_sound()
        expected_result = f"{self.m.name} makes {self.m.sound}"
        self.assertEqual(result, expected_result)

    def test_get_kingdom(self):
        result = self.m.get_kingdom()
        expected_result = self.m._Mammal__kingdom
        self.assertEqual(result, expected_result)

    def test_info(self):
        result = self.m.info()
        expected_result = f"{self.m.name} is of type {self.m.type}"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    main()