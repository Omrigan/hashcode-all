from read_write import Problem, Solution
from dummy import solve_random
from solve_tobi import solve_tobi

if __name__ == "__main__":
    p = Problem('input2019/a_example.txt')
    s = solve_tobi(p)
    print(s.check_correctness())
    s.write('output/a_example_out.txt')
    print("done")
