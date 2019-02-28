from read_write import Problem, Solution
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
