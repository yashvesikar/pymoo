from pymoo.algorithms.genetic_algorithm import GeneticAlgorithm
from pymoo.operators.default_operators import set_default_if_none, set_if_none
from pymoo.operators.survival.reference_line_survival import ReferenceLineSurvival
from pymoo.util.reference_directions import get_ref_dirs_from_points

class RNSGAIII(GeneticAlgorithm):
    def __init__(self, var_type, ref_points=None, **kwargs):
        self.ref_points = ref_points
        self.ref_dirs = None
        set_default_if_none(var_type, kwargs)
        set_if_none(kwargs, 'survival', None)
        super().__init__(**kwargs)

    def _initialize(self, problem):
        super()._initialize(problem)

        # if survival not define differently
        if self.survival is None:

            # if ref dirs are not initialized do it based on the population size
            if self.ref_dirs is None:
                self.ref_dirs = get_ref_dirs_from_points(self.ref_points, problem.n_obj)

            self.survival = ReferenceLineSurvival(self.ref_dirs)
