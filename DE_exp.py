import numpy as np
from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.optimize import minimize
from pymoo.termination import get_termination
from pymoo.operators.sampling.lhs import LHS  
from pymoo.core.problem import Problem

def objective_function(X):
    x = X[:, 0]
    y = X[:, 1]
    f = x * y**3 + 9 * x**2 - 3 * y**2 + 8
    return f  

class MyProblem(Problem):
    def __init__(self):

        super().__init__(n_var=2, n_obj=1, n_constr=0, xl=np.array([-2, -3]), xu=np.array([2, 3]))

    def _evaluate(self, X, out, *args, **kwargs):
        out["F"] = objective_function(X)

problem = MyProblem()


algorithm = DE(
    pop_size=100,  
    sampling=LHS(),  
    variant="DE/rand/1/exp", 
    CR=0.9, 
    F=0.8 
)

termination = get_termination("n_gen", 200)

result = minimize(problem,
                  algorithm,
                  termination,
                  seed=1,
                  save_history=True,
                  verbose=True)

print("Mínimo global encontrado: f(X) =", result.F[0])
