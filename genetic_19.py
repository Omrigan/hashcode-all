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


if __name__ == "__main__":
    p = Problem('input2019/e_shiny_selfies.txt')

    genetic.run_genetic(lambda: solve_random(p), sample_combinator,
                        genetic.mutator_combinator([sample_mutator], 4))
