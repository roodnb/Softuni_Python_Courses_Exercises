from unittest import TestCase, main


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Jordan Antonov', 100, 100)

    def test_init(self):
        self.assertEqual(self.worker.name, "Jordan Antonov")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_worker_work_no_energy_raises(self):
        self.worker.energy = 0
        self.assertEqual(self.worker.money, 0)
        self.assertEqual(self.worker.energy, 0)

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual(str(ex.exception), 'Not enough energy.')
        self.assertEqual(self.worker.money, 0)
        self.assertEqual(self.worker.energy, 0)

    def test_worker_works(self):
        result = self.worker.work()
        self.assertEqual(self.worker.money, 100)
        self.assertEqual(self.worker.energy, 99)
        self.assertIsNone(result)

    def test_rest(self):
        result = self.worker.rest()
        self.assertEqual(self.worker.energy, 101)
        self.assertIsNone(result)

    def test_get_info(self):

        result = self.worker.get_info()
        expected_result = "Jordan Antonov has saved 0 money."

        self.assertEqual(expected_result, result)

        self.worker.work()
        result = self.worker.get_info()
        expected_result = "Jordan Antonov has saved 100 money."
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()