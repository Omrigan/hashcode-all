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

        self.num_pics = int(next(f))
        self.orientation = []  # h/v
        self.pic_id = []  # int
        self.num_tags = []  # int
        self.tags = []  # string[]

        self.dictionary = dict()

        for i in range(self.num_pics):
            line = next(f).strip().split(' ')
            self.pic_id.append(i)
            self.orientation.append(line[ORIENT_IDX])
            self.num_tags.append(int(line[NUM_TAGS_IDX]))

            tags = set()

            for j in range(NUM_TAGS_IDX + 1, len(line)):
                tag = line[j]
                if (tag not in self.dictionary):
                    self.dictionary[tag] = len(self.dictionary)
                tags.add(self.dictionary[tag])

            self.tags.append(frozenset(tags))
        self.preprocess()

    def preprocess(self):
        self.vertical_images = []
        self.result_images = []

        sorted_vertical_tags = [[] for i in range(self.num_pics)]

        for pic_id, typ, tags in zip(self.pic_id, self.orientation, self.tags):
            if typ == 'V':
                self.vertical_images.append((pic_id, tags))
                sorted_tags = list(tags)
                sorted_tags.sort()
                sorted_vertical_tags[pic_id] = sorted_tags
            else:
                self.result_images.append((pic_id, tags))
    
        vertical_indices = [i for i in range(len(self.vertical_images))]
        random.shuffle(vertical_indices)

        pair = [-1 for i in range(len(self.vertical_images))]

        CHUNK_SIZE = 100
        used = [False for i in range(CHUNK_SIZE)]

        for ind in range(0, len(self.vertical_images), CHUNK_SIZE):
            cur_chunk_size = min(CHUNK_SIZE, len(self.vertical_images) - ind)
            
            for i in range(cur_chunk_size):
                used[i] = False

            union_sizes = []

            for i in range(cur_chunk_size):
                for j in range(cur_chunk_size):
                    if i == j:
                        continue
                    ind_i = vertical_indices[ind + i]
                    ind_j = vertical_indices[ind + j]
                    cur_union_size = len(frozenset(self.vertical_images[ind_i][1] | self.vertical_images[ind_j][1]))
                    union_sizes.append((cur_union_size, i, j))

            union_sizes.sort(reverse = True)
            
            for _, x, y in union_sizes:
                if used[x] == False and used[y] == False:
                    used[x] = True
                    used[y] = True
                    pair[vertical_indices[ind + x]] = vertical_indices[ind + y]
                    pair[vertical_indices[ind + y]] = -1

        for i in range(0, len(self.vertical_images)):
            if pair[i] != -1:
                self.result_images.append(((self.vertical_images[i][0], self.vertical_images[pair[i]][0]),
                                            frozenset(self.vertical_images[i][1] | self.vertical_images[pair[i]][1])))


class Solution:
    def __init__(self, p: Problem):
        self.p = p
        self.slideshow = []

    def add_any(self, elem):
        if type(elem) is int:
            self.slideshow.append([elem])
        else:
            self.slideshow.append(list(elem))

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

        sum = 0

        for i in range(0, len(self.slideshow) - 1):
            s1 = self.slideshow[i]
            s2 = self.slideshow[i + 1]

            if (len(s1) == 1):
                tags_s1 = self.p.tags[s1[0]]
            elif (len(s1) == 2):
                tags_s1 = self.p.tags[s1[0]] | self.p.tags[s1[1]]

            if (len(s2) == 1):
                tags_s2 = self.p.tags[s2[0]]
            elif (len(s2) == 2):
                tags_s2 = self.p.tags[s2[0]] | self.p.tags[s2[1]]

            common = len(tags_s1 & tags_s2)
            s1_only = len(tags_s1) - common
            s2_only = len(tags_s2) - common

            factor = min(common, s1_only, s2_only)
            sum += factor

        return sum
