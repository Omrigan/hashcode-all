import random

ORIENT_IDX = 0
NUM_TAGS_IDX = 1


def int_line(f):
    return tuple(int(x) for x in next(f).split(' '))


INFTY = 10 ** 9


class Problem:

    def __init__(self, filename):
        f = open(filename)

        self.num_pics = int(next(f))
        self.orientation = []  # h/v
        self.pic_id = []  # int
        self.num_tags = []  # int
        self.tags = []  # string[]

        self.dictionary = dict()

        for i in range(self.num_pics):
            line = next(f).strip().split(' ')
            self.pic_id.append(i)
            self.orientation = line[ORIENT_IDX]
            self.num_tags.append(int(line[NUM_TAGS_IDX]))

            tags = set()

            for j in range(NUM_TAGS_IDX + 1, len(line)):
                tag = line[j]
                if (tag not in self.dictionary):
                    self.dictionary[tag] = len(self.dictionary)
                tags.add(self.dictionary[tag])

            self.tags.append(tags)
        self.preprocess()

    def preprocess(self):
        self.vertical_images = []
        self.result_images = []
        for pic_id, typ, tags in zip(self.pic_id, self.orientation, self.tags):
            if typ == 'v':
                self.vertical_images.append((pic_id, tags))
            else:
                self.result_images.append((False, pic_id, tags))
        random.shuffle(self.vertical_images)
        for i in range(0, len(self.vertical_images) // 2):
            self.result_images.append((True, (self.vertical_images[2 * i][0], self.vertical_images[2 * i + 1][0]),
                                       self.vertical_images[2 * i][1] | self.vertical_images[2 * i + 1][1]))



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
