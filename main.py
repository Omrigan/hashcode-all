from read_write import Problem, Solution
import b_test_sol

if __name__ == "__main__":
    p = Problem('input2019/b_lovely_landscapes.txt')
    # s = Solution(p);
    # s.add_horizontal(0)
    # s.add_vertical(1,2)
    # s.add_horizontal(3)
    s = b_test_sol.b_test_solve(p)
    s.write('output/b_lovely_landscapes.txt')
    print("done")
