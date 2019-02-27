from read_write import Problem, Solution
from tqdm import tqdm
from pyscipopt import Model, quicksum
import random


def solve_combinatorial2(problem: Problem):
    s = Solution(problem)
    s = solve_combinatorial2_one_pass(problem, s, effective_x=problem.X / 2)
    random.shuffle(problem.requests)
    s.improvements_history.append("Second pass")
    s = solve_combinatorial2_one_pass(problem, s, effective_x=problem.X)
    return s


def solve_combinatorial2_one_pass(problem, s, effective_x):
    requests_factor = 4000
    cache_factor = 10
    for i in range(50):
        local_requests = problem.requests[i * requests_factor:(i + 1) * requests_factor]
        cache_range = range(i * cache_factor, (i + 1) * cache_factor)
        s = solve_for_subset(problem, s, local_requests, cache_range, effective_x)
        s.calculate_score()
        print(s.improvements_history)
    return s


def solve_for_subset(problem, s, local_requests, cache_range, effective_x):
    # local_requests = problem.requests[:100]
    # cache_range = range(20)
    full_cache_range = cache_range
    # full_cache_range = range(100)
    model = Model()
    # model.setRealParam('limits/time', 10)
    model.setRealParam('limits/gap', .03)
    # model.setIntParam('parallel/minnthreads', 4)
    model.setIntParam('parallel/mode', 0)
    # solver.set_time_limit(10000)

    p_vars = [{c: model.addVar('p_%s_%s' % (v, c), vtype="BINARY")
               for c in full_cache_range}
              for v in range(problem.V)]

    f_vars = []
    f_vars_server = []
    print("P initialized")

    objective = 0
    for v, e, number in tqdm(local_requests):
        req_vars = []
        for c in cache_range:
            var = model.addVar('f_%s_%s_%s' % (e, v, c), vtype="BINARY")
            objective += var * number * (s.get_minimal_latency(v, e) - problem.endpoints_caches[e][c])
            req_vars.append(var)
        f_vars.append(req_vars)
        var_server = model.addVar('f_server_%s_%s' % (e, v), vtype="BINARY")
        f_vars_server.append(var_server)
        # objective += var_server * number * problem.endpoints_server_latencies[e]
    objective = (objective / problem.total_requests) * 1000

    # Regularization term
    # objective += quicksum(quicksum(p_vars_row) for p_vars_row in p_vars)
    # # Regularization term2
    # for v_row in p_vars:
    #     for c1 in v_row[:20]:
    #         for c2 in v_row[:20]:
    #             objective -= c1 * c2

    # objective.SetMinimization()
    print("F initialized")
    #
    # Capacity
    for c in full_cache_range:
        constraint = quicksum(problem.video_sizes[v] * p_vars[v][c] for v in range(problem.V))
        model.addCons(constraint <= effective_x - s.sizes[c])
    print("Capacity done")
    #
    # # Presence
    for (v, e, number), req_vars in zip(local_requests, f_vars):
        for c, var in zip(cache_range, req_vars):
            model.addCons(var <= p_vars[v][c])
    print("Presence done")
    # From-correctness
    for server_var, req_vars in zip(f_vars_server, f_vars):
        model.addCons((quicksum(req_vars) + server_var) == 1)

    print("From-c done")

    model.setObjective(objective, "maximize")
    model.optimize()

    for v in range(problem.V):
        for c in full_cache_range:
            # print(v, c, p_vars[v][c].solution_value())

            if model.getVal(p_vars[v][c]) == 1:
                # print(model.getVal(p_vars[v][c]))
                s.cache_servers[c].append(v)
    return s
