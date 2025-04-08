from unittest import TestCase, main


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(TestCase):

    def test_init(self):
        c = Cat("Neli")

        self.assertEqual(c.name, 'Neli')
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)

    def test_cat_eats(self):
        c = Cat("Neli")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)

        result = c.eat()

        self.assertIsNone(result)
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size, 1)

    def test_cat_already_eats_raises_ex(self):
        c = Cat("Neli")
        c.eat()

        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size, 1)

        with self.assertRaises(Exception) as ex:
            c.eat()

        self.assertEqual(str(ex.exception), 'Already fed.')
        self.assertEqual(c.size, 1)
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)

    def test_cat_sleep(self):
        c = Cat("Neli")
        c.eat()
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size, 1)

        result = c.sleep()
        self.assertIsNone(result)

        self.assertTrue(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 1)

    def test_cat_sleep_raises(self):
        c = Cat("Neli")

        self.assertFalse(c.fed)
        
        with self.assertRaises(Exception) as ex:
            c.sleep()

        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')
        self.assertFalse(c.sleepy)



if __name__ == "__main__":
    main()