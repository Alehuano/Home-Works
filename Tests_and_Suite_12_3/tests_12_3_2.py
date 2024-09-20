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


import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner('Усэйн', 10)
        self.Andrey = Runner('Андрей', 9)
        self.Nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f'{key}:')
            for place, runner in result.items():
                print(f'{place}: {runner.name}')
            print()

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_Usain_Nick(self):
        tour = Tournament(90, self.Usain, self.Nick)
        result = tour.start()
        TournamentTest.all_results['Забег Усэйн и Ник'] = result
        self.assertTrue(result[max(result.keys())] == self.Nick)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_Andrey_Nick(self):
        tour = Tournament(90, self.Andrey, self.Nick)
        result = tour.start()
        TournamentTest.all_results['Забег Андрей и Ник'] = result
        self.assertTrue(result[max(result.keys())] == self.Nick)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_Usain_Andrey_Nick(self):
        tour = Tournament(90, self.Usain, self.Andrey, self.Nick)
        result = tour.start()
        TournamentTest.all_results['Общий забег'] = result
        self.assertTrue(result[max(result.keys())] == self.Nick)


if __name__ == "__main__":
    unittest.main()
