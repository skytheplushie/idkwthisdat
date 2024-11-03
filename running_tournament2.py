import unittest
from unittest import TestCase
from rt_with_exceptions import Runner, Tournament
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'тесты в этом месяце заморожены')
    def test_walk(self):
        try:
            r1 = Runner('Вася')
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50, f'{r1.name} прошёл {r1.distance} хотя должен был 50')
            logging.info('"test_walk" выполнено успешно')
        except ValueError as exc:
            logging.warning('Неверная скорость для Runner', exc_info=exc)

    @unittest.skipIf(is_frozen, 'тесты в этом месяце заморожены')
    def run_test(self):
        try:
            r2 = Runner('Коля')
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100, f'{r2.name} пробежал {r2.distance} хотя должен был 100')
            logging.info('"run_test" выполнено успешно')
        except ValueError as exc:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=exc)

    def test_challenge(self):
        r1 = Runner('Вася')
        r2 = Runner('Коля')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)
        logging.info('"test_challenge" выполнено успешно')


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'тесты в этом месяце заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.first, self.third)
        result = tournament.start()
        self.all_results['first tournament'] = result
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'тесты в этом месяце заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.second, self.third)
        result = tournament.start()
        self.all_results['second tournament'] = result
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'тесты в этом месяце заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90, self.second, self.first, self.third)
        result = tournament.start()
        self.all_results['third tournament'] = result
        self.assertTrue(result[3] == 'Ник')

    def setUp(self):
        self.first = Runner('Андрей', 10)
        self.second = Runner('Усэйн', 9)
        self.third = Runner('Ник', 3)

    @classmethod
    def tierDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{v}')