from simanneal import Annealer
from problem2017 import genetic
from dummy import solve_random
from read_write import *

from genetic_19 import sample_mutator


class MyProblem(Annealer):
    def __init__(self, solution, mutator):
        print("Base", 10 ** 6 - solution.calculate_score())
        self.mutator = mutator
        self.Tmax = 1000
        self.updates = 100
        self.steps = 100
        super(MyProblem, self).__init__(solution)

    def move(self):
        self.state = self.mutator(self.state)

    def energy(self):
        return 10 ** 6 - self.state.calculate_score()


if __name__ == "__main__":
    p = Problem('input2019/e_shiny_selfies.txt')
    ann = MyProblem(solve_random(p), genetic.mutator_combinator([sample_mutator], 2))
    result = ann.anneal()
    print(result)
