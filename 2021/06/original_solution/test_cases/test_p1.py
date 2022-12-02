import unittest
from p1 import solvep1

class test_p1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solvep1("6/example1.txt",8), 5934,
                         'Solution not ok.')

if __name__ == '__main__':
    unittest.main()
