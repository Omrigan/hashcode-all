from read_write import Problem, Solution
import os
from dummy import solve_random
from  solve_antonio import solve_antonio

INPUT_DIR = "input2019/"
OUTPUT_DIR = "output/"
FILENAMES = ["a_example.txt",
             "b_lovely_landscapes.txt",
             "c_memorable_moments.txt",
             "d_pet_pictures.txt",
             "e_shiny_selfies.txt"]


def final_solution(p):
    #return solve_random(p)
    s = solve_antonio(p, p.result_images)
    assert s.check_correctness()
    return s 


if __name__ == "__main__":
    for filename in FILENAMES:
        p = Problem(INPUT_DIR + filename)
        s = Solution(p)
        if filename == "b_lovely_landscapes.txt":
            s = b_test_sol.b_test_solve(p)
        else:
            s = final_solution(p)
        s.write(OUTPUT_DIR + filename + ".out")
        print(filename, s.calculate_score())
    os.system("zip result.zip *.py")

    # s.write('solutions/kittens.out')
