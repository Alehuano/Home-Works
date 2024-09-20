import unittest
import tests_12_3_1
import tests_12_3_2

allST = unittest.TestSuite()

allST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_1.RunnerTest))
allST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(allST)
