import unittest
from p1 import solvep1

class test_p1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solvep1("4/example1.txt",5), 4512,
                         'Solution not ok.')

if __name__ == '__main__':
    unittest.main()
