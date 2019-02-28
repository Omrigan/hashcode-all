from read_write import Problem, Solution
import sys
import tqdm

N = 80000

def dfs(v, solution, used, g):
    used[v] = True
    solution.add_horizontal(v)
    for u in g[v]:
        if used[u] == False:
            dfs(u, solution, used, g)

def b_test_solve(p):
    g = [[] for i in range(N)] 
    used = [0] * N

    sys.setrecursionlimit(N)

    tags_ids = dict()
    solution = Solution(p)

    for pic_id in tqdm.tqdm(range(p.num_pics)):
        for tag in p.tags[pic_id]:
            if tag not in tags_ids:
                tags_ids[tag] = []
            tags_ids[tag].append(pic_id)
    for tag, tag_id_list in tags_ids.items():
        assert(len(tag_id_list) <= 2)
        if len(tag_id_list) == 2:
            g[tag_id_list[0]].append(tag_id_list[1])
            g[tag_id_list[1]].append(tag_id_list[0])

    for i in range(N):
        if used[i] == False:
            dfs(i, solution, used, g)

    return solution
