import random

def int_line(f):
    return tuple(int(x) for x in next(f).split(' '))


INFTY = 10 ** 9


class Problem:

    def __init__(self, filename):
        f = open(filename)

        self.num_pics = int(next(f));
        self.pic_id = [] # int
        self.num_tags = [] # int
        self.tags = []  # string[]

        for i in range(self.num_pics):
            line = next(f).split(' ')
            self.pic_id.append(int(line[0]))
            self.num_tags.append(int(line[1]))

            tags = []

            for j in range(2, len(line)):
                tags.append(line[i])

            self.tags.append(tags)


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
