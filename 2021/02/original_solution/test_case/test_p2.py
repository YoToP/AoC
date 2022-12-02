import unittest
from p2 import solvep2

class test_p2(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solvep2("2/example1.txt"), 900,
                         'Solution not ok.')

if __name__ == '__main__':
    unittest.main()
