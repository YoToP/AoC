import unittest
from p1 import calc9Grid

class test_p1(unittest.TestCase):
    def test_example1_3D(self):
        self.assertEqual(calc9Grid([0,0,0,0,0,0,0,0,0]), 0,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([0,0,0,0,0,0,0,0,1]), 1,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([0,0,0,0,0,0,1,0,0]), 4,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([0,0,0,0,0,1,0,0,1]), 9,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([0,0,0,0,1,0,0,0,0]), 16,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([0,0,0,1,0,0,0,0,1]), 33,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([0,0,1,0,0,0,1,0,0]), 68,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([0,1,0,0,0,0,0,0,1]), 129,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([1,0,0,0,0,0,0,0,1]), 257,
                         'calc9Grid not ok.')
        self.assertEqual(calc9Grid([1,1,1,1,1,1,1,1,1]), 511,
                         'calc9Grid not ok.')
if __name__ == '__main__':
    unittest.main()
