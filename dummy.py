from read_write import Problem, Solution
import random


def solve_random(p):
    random.shuffle(p.result_images)
    s = Solution(p)
    for idx, tags in p.result_images:
        s.add_any(idx)
    return s

def evalute_pair(first, second):
    return


def solve_append_random(p):
    remaining_images = set(p.result_images)


