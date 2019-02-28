from problem2017.read_write import Problem, Solution
from problem2017.dummy import stupid_solve, solve_antonio
from tqdm import tqdm
from problem2017.combinatorial2 import solve_combinatorial2
import os

INPUT_DIR = "./problem2017/streaming/"
OUTPUT_DIR = "solutions"
FILENAMES = ["kittens.in.txt",  "me_at_the_zoo.in",  "trending_today.in",  "videos_worth_spreading.in"]


def final_solution(p):
    return Solution(p)


if __name__ == "__main__":
    totalscore=0
    for filename in FILENAMES:
        p = Problem(INPUT_DIR + filename)
        s = solve_antonio(p)
        totalscore += s.calculate_score()
        #s.write(OUTPUT_DIR + filename + ".out")
    #os.system("zip result.zip *.py")
    print(totalscore)
    # s.write('solutions/kittens.out')
