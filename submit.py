from read_write import Problem, Solution
import os

INPUT_DIR = "streaming"
OUTPUT_DIR = "solutions"
FILENAMES = ["a", "b"]


def final_solution(p):
    return Solution(p)


if __name__ == "__main__":
    for filename in FILENAMES:
        p = Problem(INPUT_DIR + filename)
        s = Solution(p)
        s.write(OUTPUT_DIR + filename + ".out")
    os.system("zip result.zip *.py")

    # s.write('solutions/kittens.out')
