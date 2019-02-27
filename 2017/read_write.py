def int_line(f):
    return tuple(int(x) for x in next(f).split(' '))


import random

INFTY = 10 ** 9


class Problem:

    def __init__(self, filename):
        f = open(filename)
        # V = number of videos
        # E = number of endpoints
        # R = number of request descriprion
        # C = number of cache servers
        # X = capacity of each cache server

        self.V, self.E, self.R, self.C, self.X = int_line(f)
        self.video_sizes = list(int_line(f))
        self.endpoints_server_latencies = []
        self.endpoints_connections = []  # endpoints_connections[cache_id] =  latency
        self.endpoints_caches = [[INFTY for i in range(self.C)] for j in range(self.E)]
        self.requests = []  # (video_id, endpoint_id, number)
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
        self._deduplicate()
        # self.requests.sort(key=lambda x: x[2], reverse=True)
        random.shuffle(self.requests)

    def _deduplicate(self):
        self.requests.sort()
        new_requests = []
        prev_request = list(self.requests[0])
        for video_id, endpoint_id, number in self.requests[1:]:
            if prev_request:
                if video_id == prev_request[0] and endpoint_id == prev_request[1]:
                    prev_request[2] += number
                else:
                    new_requests.append((tuple(prev_request)))
                    prev_request = [video_id, endpoint_id, number]
        print("Dedup requests from %s to %s" % (self.R, len(new_requests)))
        self.requests = new_requests
        self.R = len(new_requests)

    def sort_cache_endpoint(self):
        for i in range(self.E):
            self.endpoints_connections[i].sort(key=lambda x: x[1], reverse=True)


class Solution:
    def __init__(self, p: Problem):
        self.p = p
        self.cache_servers = [[] for i in range(p.C)]
        self.sizes = [0 for i in range(p.C)]
        self.request_minimal_latencies = {}
        self.improvements_history = []

    def possible(self, c, v):
        return (self.sizes[c] + self.p.video_sizes[v] < self.p.X) and v not in self.cache_servers[c]

    def normalize_sizes(self):
        self.sizes = [sum(self.p.video_sizes[v] for v in serv)
                      for serv in self.cache_servers]

    def attach(self, c, v):
        self.cache_servers[c].append(v)
        self.sizes[c] += self.p.video_sizes[v]

    def drop(self, c):
        self.sizes[c] -= self.p.video_sizes[self.cache_servers[c][-1]]
        self.cache_servers[c].pop(-1)

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
                size += self.p.video_sizes[video]

            if size > self.p.X:
                print("Solution incorrect. Video %s, size %s, max %s" % (video, size, self.p.X))
                return False
            if len(server) > len(set(server)):
                print("Solution incorrect, video duplicate. Video %s, size %s, max %s" % (video, size, self.p.X))
                return False

        return True

    def get_minimal_latency(self, v, e):
        return self.request_minimal_latencies.get((v, e)) or self.p.endpoints_server_latencies[e]

    def calculate_score(self, check_correctness=True):
        if check_correctness:
            assert self.check_correctness()
        video_to_servers = [[] for i in range(self.p.V)]
        for i, server in enumerate(self.cache_servers):
            for video in server:
                video_to_servers[video].append(i)
        total_improve = 0
        for v, e, c in self.p.requests:
            baseline_latency = self.p.endpoints_server_latencies[e]
            minmal_latency = baseline_latency
            for server in video_to_servers[v]:
                minmal_latency = min(minmal_latency, self.p.endpoints_caches[e][server])
            if minmal_latency < baseline_latency:
                self.request_minimal_latencies[(v, e)] = minmal_latency
            total_improve += (baseline_latency - minmal_latency) * c
        total_improve /= self.p.total_requests
        total_improve *= 1000
        self.improvements_history.append(total_improve)
        return total_improve
