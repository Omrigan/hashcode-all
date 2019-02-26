from ortools.linear_solver import pywraplp
from read_write import Problem, Solution
from tqdm import tqdm


def solve_combinatorial(problem: Problem):
    local_requests = problem.requests[:1000]
    cache_range = range(10)
    
    solver = pywraplp.Solver('SolveIntegerProblem',
                             pywraplp.Solver.BOP_INTEGER_PROGRAMMING,)
    # solver.set_time_limit(10000)

    p_vars = [[solver.IntVar(0.0, 1, 'p_%s_%s' % (v, c))
               for c in cache_range]
              for v in range(problem.V)]

    f_vars = []
    print("P initialized")

    objective = solver.Objective()
    for v, e, number in tqdm(local_requests):
        req_vars = []
        for c in cache_range:
            var = solver.IntVar(0.0, 1, 'f_%s_%s_%s' % (e, v, c))
            objective.SetCoefficient(var, number * problem.endpoints_caches[e][c])
            req_vars.append(var)
        f_vars.append(req_vars)
    objective.SetMinimization()
    print("F initialized")

    # Capacity
    for c in cache_range:
        constraint = solver.Constraint(-solver.infinity(), problem.X)
        for v in range(problem.V):
            size = problem.video_sizes[v]
            constraint.SetCoefficient(p_vars[v][c], size)
    print("Capacity done")

    # Presence
    for (v, e, number), req_vars in zip(local_requests, f_vars):
        for c, var in zip(cache_range, req_vars):
            constraint = solver.Constraint(0, solver.infinity())
            constraint.SetCoefficient(p_vars[v][c], 1)
            constraint.SetCoefficient(var, -1)
    print("Presence done")
    # From-correctness
    for req_vars in f_vars:
        constraint = solver.Constraint(1, 1)
        for var in req_vars:
            constraint.SetCoefficient(var, 1)
    print("From-c done")

    """Solve the problem and print the solution."""
    result_status = solver.Solve()
    # The problem has an optimal solution.
    # assert result_status == pywraplp.Solver.OPTIMAL

    # The solution looks legit (when using solvers other than
    # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
    assert solver.VerifySolution(1e-7, True)

    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())

    # The objective value of the solution.
    print('Optimal objective value = %d' % solver.Objective().Value())
    print()

    s = Solution(problem)

    for v in range(problem.V):
        for c in cache_range:
            # print(v, c, p_vars[v][c].solution_value())
            if p_vars[v][c].solution_value() > 0:
                s.cache_servers[c].append(v)
    return s
    # The value of each variable in the solution.
    # variable_list = [x, y]

    # for variable in variable_list:
    #   print('%s = %d' % (variable.name(), variable.solution_value()))
