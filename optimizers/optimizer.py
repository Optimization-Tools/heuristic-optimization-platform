import logging
from utilities import logger as lg
from optimizers.variator import Variator
from optimizers.crossover import Crossover
import copy


class Optimizer:
    def __init__(self, **kwargs):
        # Persist current configuration and problem
        self.random = kwargs['random']
        self.hj = kwargs['hopjob']

    def run(self, **kwargs):
        self.pre_processing(**kwargs)
        self.optimize()
        self.post_processing(**kwargs)

    def get_generator(self):
        if self.hj.pid_type == 'combinatorial':
            return self.hj.generator_comb
        else:
            return self.hj.generator_cont

    def binary_to_float(self, binary):
        # Transform bit string to float
        float_vals = []
        for b in binary:
            fv = float(int(''.join([str(i) for i in b]), 2))

            # Rescale float within lower and upper bounds of
            fv = fv / (2 ** self.hj.bit_computing - 1) * (self.hj.pid_ub - self.hj.pid_lb) + self.hj.pid_lb
            float_vals.append(fv)
        return float_vals

    def pre_processing(self, **kwargs):
        pass

    def post_processing(self, **kwargs):
        pass
