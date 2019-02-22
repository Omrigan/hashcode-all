def int_line(f):
    return tuple(int(x) for x in next(f).split(' '))
INFTY = 10**9
class Problem:

    def __init__(self, filename):
        f = open(filename)
        #V = number of videos
        #E = number of endpoints  
        #R = number of request descriprion
        #C = number of cache servers
        #X = capacity of each cache server

        self.V, self.E, self.R, self.C, self.X = int_line(f)
        self.video_sizes = list(int_line(f))
        self.endpoints_server_latencies = []
        self.endpoints_connections = [] # endpoints_connections[cache_id] =  latency
        self.endpoints_caches = [[INFTY for i in range(self.C)] for j in range(self.E)]
        self.requests = [] # (video_id, endpoint_id, number)
        self.total_requests = 0
        
        for i in range(self.E):
            latency, number_of_cons = int_line(f)
            self.endpoints_server_latencies.append(latency)
            cons = []
            for j in range(number_of_cons):
                cache_id, latency = int_line(f)
                cons.append((cache_id, latency))
                self.endpoints_caches[i][cache_id] = latency
            self.endpoints_connections.append(cons)
        for i in range(self.R):
            self.requests.append(int_line(f))
            self.total_requests += self.requests[-1][2]

class Solution:
    def __init__(self, p : Problem):
        self.p = p
        self.cache_servers = [[] for i in range(p.C)]
        self.sizes = [ 0 for i in range(p.C)]
    
    def attach(self,c,v):
        self.cache_servers[c].append(v)
        self.sizes[c] += self.p.video_sizes[v]

    def write(self, filename):
        f = open(filename, 'w')
        f.write("%s\n" % len(self.cache_servers))
        for i in range(len(self.cache_servers)):
            f.write("%s " % i)
            f.write(" ".join(str(x) for x in self.cache_servers[i]))
            f.write("\n")

    def check_correctness(self):
        for server in self.cache_servers:
            size = 0
            for video in server:
                size+=self.p.video_sizes[video]
            if size>self.p.X:
                print("Solution incorrect. Video %s, size %s, max %s" % (video, size, self.p.X))
                return False
        return True
    
    def calculate_score(self):
        video_to_servers = [[] for i in range(self.p.V)]
        for i, server in enumerate(self.cache_servers):
            for video in server:
                video_to_servers[video].append(i)
        total_improve = 0
        for req in self.p.requests:
            baseline_latency = self.p.endpoints_server_latencies[req[1]]
            minmal_latency = baseline_latency
            for server in video_to_servers[req[0]]:
                minmal_latency = min(minmal_latency, self.p.endpoints_caches[req[1]][server])
            total_improve+=(baseline_latency-minmal_latency)*req[2]
        total_improve/=self.p.total_requests
        total_improve*=1000
        return total_improve





        

        

            

        

