import random

ORIENT_IDX = 0
NUM_TAGS_IDX = 1


def increase_dict_count(dict, id):
    if (id not in dict):
        dict[id] = 1;
        return True
    else:
        dict[id] = dict[id] + 1
        return False


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
            self.orientation.append(line[ORIENT_IDX])
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
        ids = dict()
        for i in range(len(self.slideshow)):
            slide = self.slideshow[i]
            if (len(slide) == 1):
                id = slide[0]
                if (id < 0 or id >= len(self.p.orientation)):
                    return False
                if (not increase_dict_count(ids, id)):
                    return False
                if (self.p.orientation[id] != 'H'):
                    return False
            elif (len(slide) == 2):
                id1 = slide[0]
                id2 = slide[1]
                if (id1 < 0 or id1 >= len(self.p.orientation)):
                    return False
                if (id1 < 0 or id2 >= len(self.p.orientation)):
                    return False
                if (not increase_dict_count(ids, id1) or
                    not increase_dict_count(ids, id2)):
                    return False
                if (self.p.orientation[id1] != 'V' or
                    self.p.orientation[id2] != 'V'):
                    return False


        return True

    def calculate_score(self):
        assert self.check_correctness()
        return 0
