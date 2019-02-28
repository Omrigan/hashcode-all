import random

def int_line(f):
    return tuple(int(x) for x in next(f).split(' '))


INFTY = 10 ** 9


class Problem:

    def __init__(self, filename):
        f = open(filename)



class Solution:
    def __init__(self, p: Problem):
        self.p = p

    def write(self, filename):
        pass

    def check_correctness(self):
        return True

    def calculate_score(self):
        assert self.check_correctness()
        return 0
