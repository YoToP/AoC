import unittest
from p2 import solvep2

class test_p1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solvep2("15/example1.txt",5), 315,
                         'Solution not ok.')
if __name__ == '__main__':
    unittest.main()
