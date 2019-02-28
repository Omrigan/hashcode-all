from read_write import Problem, Solution

def score(tags_s1, tags_s2):
    common = len(tags_s1 & tags_s2)
    s1_only = len(tags_s1) - common
    s2_only = len(tags_s2) - common

    factor = min(common, s1_only, s2_only)
    return factor

MAX_RANGE = 100

def solve_tobi(p: Problem):
    s = Solution(p)
    current = None
    remaining_pics = []
    for i in range(p.num_pics):
        if (p.orientation[i] != 'H'):
            continue # for now only horizontal

        # init first
        if (current == None):
            current = p.tags[i]
            s.add_horizontal(i)
            remaining_pics = set(range(i + 1, p.num_pics))

        best_candidate = -1
        best_score = -1

        for j in remaining_pics:
            candidate_id = j
            if (p.orientation[candidate_id] != 'H'):
                continue # for now only horizontal
            candidate = p.tags[candidate_id]
            score_candidate = score(current, candidate)
            if (score_candidate > best_score):
                best_candidate = candidate_id
                best_score = score_candidate

        if best_candidate != -1:
            s.add_horizontal(best_candidate)
        remaining_pics = remaining_pics - set([best_candidate])

    return s