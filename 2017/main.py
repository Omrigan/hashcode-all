from read_write import Problem, Solution
from dummy import stupid_solve
from tqdm import tqdm
from combinatorial2 import solve_combinatorial2


def solve_antoio(p: Problem):
    s = Solution(p)
    sorted_requests = sorted(p.requests, key=lambda r1: r1[2] * p.endpoints_server_latencies[r1[1]])
    for r in tqdm(sorted_requests):
        endpoint = r[1]
        video = r[0]
        cache_servers = p.endpoints_connections[endpoint]
        cache_servers.sort(key=lambda x: x[1])
        for c in cache_servers:
<<<<<<< HEAD
            if video not in c:
                if s.sizes[c[0]] + p.video_sizes[video] < p.X:
                    s.attach(c[0] ,video)
                    break  
    print(s.cache_servers)
=======
            if s.possible(c[0], video):
                s.attach(c[0], video)
                break
>>>>>>> 3a4a44224c6fde873b0d61cb08f01435bc9e0b13
    return s


'''    
    for c in range(p.C):
        total_sum = 0
        this_server_videos = set()
        print (c)
        #while True:
        #   
        #    s.cache_servers[]

'''

if __name__ == "__main__":
    p = Problem('streaming/kittens.in.txt')
    s = solve_combinatorial2(p)
    s.write("solutions/kittens-combinatorial.out")
    print("Combinatorial", s.calculate_score())
    s = solve_antoio(p)
    print("Antonio", s.calculate_score())
    s = stupid_solve(p)
    print("Stupid", s.calculate_score())
    # s.write('solutions/kittens.out')
