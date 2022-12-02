import unittest
from p2 import solvep2

class test_p2(unittest.TestCase):
    '''def test_example1(self):
        self.assertEqual(solvep1("18/simple1.txt"), 40,
                         'Solution not ok.')'''
    def test_example1(self):
        self.assertEqual(solvep2("18/example2.txt"), 3993,
                         'Solution not ok.')
if __name__ == '__main__':
    unittest.main()
