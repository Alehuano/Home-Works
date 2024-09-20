import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    @unittest.skipIf(False, 'Проверяем')
    def test_walk(self):
        walker = Runner('Oksana')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(False, 'Проверяем')
    def test_run(self):
        runner = Runner('Leo')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(False, 'Проверяем')
    def test_challenge(self):
        runner = Runner('Leo')
        walker = Runner('Oksana')
        for i in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(runner.distance, walker.distance, 'Тест не пройден')
