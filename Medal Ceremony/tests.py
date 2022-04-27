from solution import MedalCeremony
import unittest


class MedalCeremonyTests(unittest.TestCase):

    def test1(self):
        result = MedalCeremony()
        self.assertEqual(result.count_possible_interviews(["-12,4,8:56", "3,-3,11:06", "-11,3,12:21", "-5,10,13:16"]),
                         4)


if __name__ == '__main__':
    unittest.main()