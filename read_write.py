import random

ORIENT_IDX = 0
NUM_TAGS_IDX = 1


def int_line(f):
    return tuple(int(x) for x in next(f).split(' '))


INFTY = 10 ** 9


class Problem:

    def __init__(self, filename):
        f = open(filename)

        self.num_pics = int(next(f));
        self.orientation = [] # h/v
        self.pic_id = [] # int
        self.num_tags = [] # int
        self.tags = []  # string[]

        self.dictionary = dict()

        for i in range(self.num_pics):
            line = next(f).strip().split(' ')
            self.pic_id.append(i)
            self.orientation = line[ORIENT_IDX]
            self.num_tags.append(int(line[NUM_TAGS_IDX]))

            tags = []

            for j in range(NUM_TAGS_IDX + 1, len(line)):
                tag = line[j]
                if (tag not in self.dictionary):
                    self.dictionary[tag] = len(self.dictionary)
                tags.append(self.dictionary[tag])

            self.tags.append(tags)


class Solution:
    def __init__(self, p: Problem):
        self.p = p
        self.slideshow = []

    def add_horizontal(self, id):
        self.slideshow.append([id])

    def add_vertical(self, id1, id2):
        self.slideshow.append([id1, id2])

    def write(self, filename):
        f = open(filename, 'w')
        f.write("%s\n" % len(self.slideshow))
        for i in range(len(self.slideshow)):
            slide = self.slideshow[i]
            if (len(self.slideshow[i]) == 1):
                f.write("%d\n" % slide[0]);
            elif (len(self.slideshow[i]) == 2):
                f.write("%d %d\n" % (slide[0], slide[1]))
        pass

    def check_correctness(self):
        return True

    def calculate_score(self):
        assert self.check_correctness()
        return 0
