from unittest import TestCase


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

class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_first_tournament(self):
        tournament = Tournament(90, self.first, self.third)
        result = tournament.start()
        self.all_results['first tournament'] = result
        self.assertTrue(result[2] == 'Ник')

    def test_second_tournament(self):
        tournament = Tournament(90, self.second, self.third)
        result = tournament.start()
        self.all_results['second tournament'] = result
        self.assertTrue(result[2] == 'Ник')

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