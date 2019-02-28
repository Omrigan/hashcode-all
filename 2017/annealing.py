from simanneal import Annealer
from read_write import Problem, Solution
from genetic import sample_mutator, other_mutator, mutator_combinator
from dummy import stupid_solve


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
    p = Problem('streaming/kittens.in.txt')
    ann = MyProblem(stupid_solve(p), mutator_combinator([sample_mutator, other_mutator], 2))
    result = ann.anneal()
    print(result)
