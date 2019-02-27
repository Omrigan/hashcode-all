from read_write import *
import random

from read_write import Problem, Solution
from dummy import stupid_solve

POPULATION_SIZE = 20
MUTATION_PROB = 1
MUTATION_MAX = 10
ITERATIONS = 30
SELECTION_CHANGE = int(POPULATION_SIZE * 0.5)


def recombinate(population, combinator):
    for i in range(POPULATION_SIZE):
        a = random.randrange(POPULATION_SIZE)
        b = random.randrange(POPULATION_SIZE)
        population.append(combinator(population[a], population[b]))

    return population


def mutate(population, mutator):
    for i in range(POPULATION_SIZE):
        if random.random() < MUTATION_PROB:
            for i in range(random.randrange(MUTATION_MAX)):
                population[i] = mutator(population[i])
    return population


def select(population):
    population = sorted(((obj.calculate_score(False), obj) for obj in population),
                        key=lambda x: x[0], reverse=True)
    new_population = [(i + random.randrange(SELECTION_CHANGE), obj) for i, (score, obj) in enumerate(population)]
    new_population.sort(key=lambda x: x[0])
    return [obj for _, obj in new_population[:POPULATION_SIZE]]


def print_scores_formatted(population):
    print("Scores: " + " ".join([str(obj.calculate_score()) for obj in population[:10]]))


def run_genetic(initial_generator, combinator, mutator):
    """
    :param initial_generator:  ->Solution
    :param combinator: (Solution,Solution)->Solution
    :param mutator: Solution->Solution
    :return:
    """
    population = [initial_generator() for i in range(POPULATION_SIZE)]
    for i in range(ITERATIONS):
        print("Step:", i)
        print_scores_formatted(population)
        population = recombinate(population, combinator)
        print("Recombination done")
        # print_scores_formatted(population)
        population = mutate(population, mutator)
        print("Mutation done")
        # print_scores_formatted(population)
        population = select(population)
        print("Selection done")
        # print_scores_formatted(population)
    return population[0]


def sample_combinator(sol1, sol2):
    result_solution = Solution(sol1.p)
    for i in range(sol1.p.C):
        if random.random() < 0.5:
            result_solution.cache_servers[i] = sol1.cache_servers[i]
        else:
            result_solution.cache_servers[i] = sol2.cache_servers[i]
    # result_solution.normalize_sizes()
    return result_solution


def sample_mutator(sol):
    v = random.randrange(sol.p.V)
    c = random.randrange(sol.p.C)
    if sol.p.video_sizes[v] > sol.p.X:
        raise Exception("Mutator error")
    sol.normalize_sizes()
    while not sol.possible(c, v):
        sol.drop(c)
    sol.attach(c, v)
    return sol


if __name__ == "__main__":
    p = Problem('streaming/kittens.in.txt')
    run_genetic(lambda: stupid_solve(p), sample_combinator, sample_mutator)
