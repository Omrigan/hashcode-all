from read_write import Problem, Solution

def stupid_solve(p):
    s = Solution(p)
    for c in range(p.C):
        total_sum = 0
        this_server_videos = set()
        while True:
            
            s.cache_servers[]

if __name__ == "__main__":    
    p = Problem('streaming/kittens.in.txt')
    s = stupid_solve(p)
    assert s.check_correctness()
    print(s.calculate_score())
    s.write('solutions/kittens.out')


