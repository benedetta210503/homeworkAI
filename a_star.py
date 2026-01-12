import time
import heapq
from node import *
from problem import *

def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))


def heuristic_conflicts(state, n):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def heuristic(state, n):
    return n - len(state)

def a_star(problem, heuristic_fn):

    start_time = time.time()

    start_state = problem.initial_state()
    node = Node(
        state=start_state,
        g=0,
        h=heuristic_fn(start_state, problem.n)
    )

    frontier = []
    heapq.heappush(frontier, node)
    frontier_states = {node.state: node}
    explored = set()

    
    expanded_nodes = 0
    generated_nodes = 0
    max_nodes_in_memory = 1

    while frontier:
        n = heapq.heappop(frontier)
        frontier_states.pop(n.state, None)

        if problem.goal_test(n.state):
            end_time = time.time()
            
            metrics = {
                'expanded': expanded_nodes,
                'generated': generated_nodes,
                'max_memory': max_nodes_in_memory,
                'time': end_time - start_time
            }
            return reconstruct_path(n), metrics

        explored.add(n.state)
        expanded_nodes += 1

        available_actions = problem.actions(n.state)
        num_children = len(available_actions)

        for action in available_actions:
            child_state = problem.result(n.state, action)
            g_child = n.g + problem.step_cost(n.state, action)
            h_child = heuristic_fn(child_state, problem.n)

            child = Node(state=child_state, parent=n, action=action, g=g_child, h=h_child)
            generated_nodes += 1

            if child.state not in explored and child.state not in frontier_states:
                heapq.heappush(frontier, child)
                frontier_states[child.state] = child
            elif child.state in frontier_states:
                if child.g < frontier_states[child.state].g:
                    frontier.remove(frontier_states[child.state])
                    heapq.heapify(frontier)
                    heapq.heappush(frontier, child)
                    frontier_states[child.state] = child

        max_nodes_in_memory = max(max_nodes_in_memory, len(frontier) + len(explored))

    end_time = time.time()
    metrics = {
        'expanded': expanded_nodes,
        'generated': generated_nodes,
        'max_memory': max_nodes_in_memory,
        'time': end_time - start_time
    }
    return None, metrics
