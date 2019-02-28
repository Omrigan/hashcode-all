from read_write import Problem, Solution
from dummy import stupid_solve
from tqdm import tqdm
#from combinatorial import solve_combinatorial


def solve_antoio(p: Problem):
    s = Solution(p)
    #lambda = numebr of request * distance main server
    sorted_requests = sorted(p.requests, key=lambda r1: r1[2] * p.endpoints_server_latencies[r1[1]])
    for r in tqdm(sorted_requests):
        endpoint = r[1]
        video = r[0]
        cache_servers = p.endpoints_connections[endpoint]
        cache_servers.sort(key=lambda x: x[1])
        for c in cache_servers:
            if s.possible(c[0], video):
                s.attach(c[0], video)
                break
    return s

def solve_antoio_NEW(p: Problem):
    s = Solution(p)
    #GAIN -> lambda = 
    sorted_requests = sorted(p.requests, key=lambda r1: r1[2] * p.endpoints_server_latencies[r1[1]])
    for r in tqdm(sorted_requests):
        endpoint = r[1]
        video = r[0]
        cache_servers = p.endpoints_connections[endpoint]
        cache_servers.sort(key=lambda x: x[1])
        for c in cache_servers:
            if s.possible(c[0], video):
                s.attach(c[0], video)
                break
    return s

def improve_antonio_solution_with_genetic(s : Solution):

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
    #s = solve_combinatorial(p)
    #s.write("solutions/kittens-combinatorial.out")
    #print("Combinatorial", s.calculate_score())
    s = solve_antoio(p)
    print("Antonio", s.calculate_score())
    s = stupid_solve(p)
    print("Stupid", s.calculate_score())
    # s.write('solutions/kittens.out')
