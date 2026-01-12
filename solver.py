from z3 import Solver, Int, Distinct, Abs, sat
import time 
def solve_n_queens_csp(problem):
    n = problem.n
    queens = [Int(f"Q{i}") for i in range(n)]
    solver = Solver()

    solver.add(Distinct(queens))

    for i in range(n):
        solver.add(queens[i] >= 0, queens[i] < n)
        for j in range(i+1, n):
            solver.add(Abs(queens[i] - queens[j]) != j - i)  
    
    start_time = time.time()
    result = solver.check()
    end_time = time.time()
    
    stats = solver.statistics()

    metrics = {
        "N": n,
        "time_s": end_time - start_time,
        "num_assertions": len(solver.assertions()),
        "decisions": stats.get_key_value("decisions"),
        "conflicts": stats.get_key_value("conflicts"),
        "propagations": stats.get_key_value("propagations")
    }
    if result == sat:
        model = solver.model()
        solution = tuple(model.evaluate(q).as_long() for q in queens)
        return solution, metrics
    else:
        return None, metrics
