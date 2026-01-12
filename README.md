# homeworkAI
# N-Queens Problem 

This project focuses on solving the **N-Queens problem** using two different  approaches:

- **A\*** search algorithm  
- **Constraint Satisfaction Problem (CSP)** formulation using the Z3 solver

The goal of the N-Queens problem is to place `N` queens on an `N x N` chessboard such that no two queens attack each other.
Two queen attack each other when they are in the same row, or in the same column or in the same diagonal.

---

### A* Search
The problem is, with this approach, threated as a state-space search problem.
Each state consists of a partial or total positioning of the queens.
In the A* algorithm, a heuristic function is used, which, together with the cost, guides and directs the order of node expansions and the management of the frontier. The algorithm returns the solution path, that is, the placement of the N queens, and prints some important metrics used to evaluate its performance, if it finds a solution, that is, a suitable placement of the queens that ensures no conflicts. If it does not find any solution, the algorithm returns None along with the previous metrics.

### Constraint Satisfaction Problem (CSP)
The problem is formulated as a CSP where:
- Each queen position is a variable.
- Constraints ensure that no two queens attack each other.
- The **Z3 SMT solver** is used to find a valid assignment.
## Visualization and Animation

The project includes a visualization of the chessboard using **matplotlib**.

- The board configuration can be visualized for both approaches, CSP and A*.
- For the **A\*** approach, the solution is shown **step by step** through an **animated visualization** and allows you to see at each step how the queen is positioned.

## Results
At the end of a sequence of experiments in which the parameter N, that is, the size of the chessboard, is varied, three graphs are shown for the A* algorithm indicating the variation in the number of nodes generated, the variation in the number of nodes explored, and the running time. As for the Z3 solver, an indicative table is printed at the end showing the main metrics and the running time.

## How to Run the Project

The project is designed to be executed from the command line and allows the user to **interactively choose**:

- The solving approach (**A\*** or **CSP**)
- The board size (`N`)
- Optionally, a **list of board sizes** to run multiple experiments
- (For A\*) the **heuristic function** to be used

---

## Dependencies

To run this project, you need:

- **Python 3.8 or higher**
- **matplotlib** (for visualization and animation)
- **z3-solver** (for CSP solving)

Install all dependencies using:

```bash
pip install matplotlib z3-solver






