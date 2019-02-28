from read_write import Problem, Solution
from dummy import solve_random

if __name__ == "__main__":
    p = Problem('input2019/a_example.txt')
    s = solve_random(p)
    # s.add_horizontal(0)
    # s.add_vertical(1, 2)
    # s.add_horizontal(3)
    s.write('output/a_example_out.txt')
    print("done")
