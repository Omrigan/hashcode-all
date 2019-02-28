from problem2017.read_write import Problem, Solution
from tqdm import tqdm
import random


def stupid_solve(p: Problem):
    s = Solution(p)
    for c in range(p.C):
        total_sum = 0
        this_server_videos = set()
        while True:
            video_idx = random.randrange(p.V)
            if video_idx in this_server_videos:
                break
            # print(len(p.video_sizes), video_idx)
            if (total_sum + p.video_sizes[video_idx]) > p.X:
                break
            total_sum += p.video_sizes[video_idx]
            this_server_videos.add(video_idx)

        assert s.check_correctness()
        s.cache_servers[c] = list(this_server_videos)
    return s

def solve_antonio(p: Problem):
    s = Solution(p)
    #lambda = numebr of request * distance main server
    sorted_requests = sorted(p.requests, key=lambda r1: r1[2] * p.endpoints_server_latencies[r1[1]])
    #for i in range(p.C):
    #    p.endpoints_connections[i].sort(key=lambda x: x[1])
    for i in range(p.C):
        p.endpoints_connections[i].sort(key=lambda x: x[1])
    for r in tqdm(sorted_requests):
        endpoint = r[1]
        video = r[0]
        cache_servers = p.endpoints_connections[endpoint]
        cache_servers.sort(key=lambda x: x[1])
        for c in cache_servers:
            if s.possible(c[0], video):
            s.attach(c[0], video)
                #break
    return s
