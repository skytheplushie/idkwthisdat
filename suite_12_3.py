import unittest
import running_tournament

runner_suite = unittest.TestSuite()
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(running_tournament.RunnerTest))
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(running_tournament.TournamentTest))



runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_suite)