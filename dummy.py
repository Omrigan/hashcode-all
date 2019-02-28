from read_write import Problem, Solution
import random


def solve_random(p):
    random.shuffle(p.result_images)
    s = Solution(p)
    for idx, tags in p.result_images:
        if type(idx) is int:
            s.add_any([idx])
        else:
            s.add_any(list(idx))
    return s

def solve_append_random(p):
    remaining_images = set()
