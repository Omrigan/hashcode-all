from read_write import Problem, Solution
from dummy import stupid_solve
if __name__ == "__main__":    
    p = Problem('streaming/kittens.in.txt')
    s = stupid_solve(p)
    assert s.check_correctness()
    print(s.calculate_score())
    s.write('solutions/kittens.out')


