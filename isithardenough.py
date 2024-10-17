from unittest import TestCase


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


class Runner_Test(TestCase):
    def test_walk(self):
        r1 = Runner("Gosha")
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50, f'{r1.name} walked till {r1.distance}, '
                                          f'though should have walked till 50')

    def test_challenge(self):
        r1 = Runner("Gosha")
        r2 = Runner("Gleb")
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)