from problem2017 import genetic
from dummy import solve_random
from read_write import *


def sample_combinator(sol1, sol2):
    return sol1


def sample_mutator(sol):
    first = random.randrange(len(sol.slideshow))
    second = random.randrange(len(sol.slideshow))
    sol.slideshow[first], sol.slideshow[second] = sol.slideshow[second], sol.slideshow[first]

    return sol


def other_mutator(sol):
    a = random.randrange(sol.p.C)
    b = random.randrange(sol.p.C)
    sol.cache_servers[a], sol.cache_servers[b] = sol.cache_servers[b], sol.cache_servers[a]
    sol.normalize_sizes()
    return sol


if __name__ == "__main__":
    p = Problem('problem2017/streaming/kittens.in.txt')
    genetic.run_genetic(lambda: solve_random(p), sample_combinator,
                        genetic.mutator_combinator([sample_mutator, other_mutator], 4))
