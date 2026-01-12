from a_star import *
from node import *
from problem import *
from solver import *
from animation import *
import matplotlib.pyplot as plt


def parse_n_values(input_str):
    try:
        if "," in input_str:
            return [int(x.strip()) for x in input_str.split(",")]
        else:
            return [int(input_str.strip())]
    except ValueError:
        raise ValueError("Invalid input for board size(s).")


def choose_approach():
    while True:
        choice = input("Choose approach (A* / CSP): ").strip().lower()
        if choice in ["a*", "astar", "a"]:
            return "astar"
        elif choice == "csp":
            return "csp"
        else:
            print("Invalid choice. Please enter A* or CSP.")


def choose_heuristic():
    while True:
        print("\nChoose heuristic for A*:")
        print("1 - Number of remaining queens")
        print("2 - Number of conflicts")

        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            return heuristic
        elif choice == "2":
            return heuristic_conflicts
        else:
            print("Invalid heuristic choice.")


def main():

    print("=== N-Queens Problem Solver ===\n")

    approach = choose_approach()
    heuristic = None

    if approach == "astar":
        heuristic = choose_heuristic()

    n_input = input("\nEnter board size (e.g. 8) or list (e.g. 4,8,12): ")
    n_values = parse_n_values(n_input)

    results = []

    for n in n_values:
        print(f"\n=== Solving N = {n} ===")

        problem = N_Queens(n)

        # ---------- CSP ----------
        if approach == "csp":
            solution, metrics = solve_n_queens_csp(problem)

            print("Time (s):", metrics["time_s"])
            print("Number of assertions:", metrics["num_assertions"])
            print("Solution:", solution)
            print("Time (s):", metrics["time_s"])
            print("Number of assertions:", metrics["num_assertions"])
            print("Decisions:", metrics["decisions"])
            print("Conflicts:", metrics["conflicts"])
            print("Propagations:", metrics["propagations"])

        elif approach == "astar":
            solution, metrics = a_star(problem, heuristic)
            print("Solution found:", solution)
            print("Metrics:", metrics)
            results.append({'n': n, **metrics})
            animate_solution(solution, n)

    if approach == "astar" and len(results) > 1:
        print("\nSummary table:")
        print(f"{'N':>3} | {'Expanded':>10} | {'Generated':>10} | {'Max Mem':>10} | {'Time (s)':>8}")
        print("-" * 55)

        for r in results:
            print(f"{r['n']:>3} | {r['expanded']:>10} | {r['generated']:>10} | "
                  f"{r['max_memory']:>10} | {r['time']:>8.4f}")

        n_list = [r['n'] for r in results]
        expanded_list = [r['expanded'] for r in results]
        generated_list = [r['generated'] for r in results]
        time_list = [r['time'] for r in results]

        plt.figure()
        plt.plot(n_list, expanded_list, marker='o')
        plt.title('Expanded Nodes by N')
        plt.xlabel('N')
        plt.ylabel('Expanded Nodes')
        plt.grid(True)
        plt.show()

        plt.figure()
        plt.plot(n_list, generated_list, marker='o')
        plt.title('Generated Nodes by N')
        plt.xlabel('N')
        plt.ylabel('Generated Nodes')
        plt.grid(True)
        plt.show()

        plt.figure()
        plt.plot(n_list, time_list, marker='o')
        plt.title('A* Running Time by N')
        plt.xlabel('N')
        plt.ylabel('Time (seconds)')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    main()
