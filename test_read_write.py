import unittest
from read_write import Problem, Solution

class TestReadWrite(unittest.TestCase):
    def test1(self):
        p = Problem('input2019/a_example.txt')
        s = Solution(p);
        s.add_horizontal(1)
        s.add_vertical(1,2)
        s.add_horizontal(3)
        self.assertFalse(s.check_correctness())

    def test2(self):
        p = Problem('input2019/a_example.txt')
        s = Solution(p);
        s.add_horizontal(1)
        self.assertFalse(s.check_correctness())

    def test3(self):
        p = Problem('input2019/a_example.txt')
        s = Solution(p);
        s.add_horizontal(4)
        self.assertFalse(s.check_correctness())

    def test4(self):
        p = Problem('input2019/a_example.txt')
        s = Solution(p);
        s.add_horizontal(0)
        s.add_horizontal(3)
        self.assertTrue(s.check_correctness())

    def test5(self):
        p = Problem('input2019/a_example.txt')
        s = Solution(p);
        s.add_vertical(1,2)
        self.assertTrue(s.check_correctness())

if __name__ == "__main__":
    unittest.main()