from day18 import calcSurface
from day18 import part2

def test_1_cube():
    assert calcSurface([[1,1,1]]) == 6

def test_2_cubes():
    assert calcSurface([[1,1,1],[2,1,1]]) == 10

def test_3_cubes():
    assert calcSurface([[1,1,1],[2,1,1],[3,1,1]]) == 14

def test_2_sep_cubes():
    assert calcSurface([[1,1,1],[3,1,1]]) == 12

def testp2_calcSurface():
    assert calcSurface([[1,0,1],[0,1,1],[2,1,1],[1,1,0],[1,1,2],[1,2,1]]) == 36

def testp2_missingCube():
    assert part2("2022/18/inputs/test1.txt") == 30