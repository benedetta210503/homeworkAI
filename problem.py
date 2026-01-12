
def count_conflicts(state, n):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts


class N_Queens:
    def __init__(self, n):
        self.n = n

    def initial_state(self):
        return ()  
      
    def goal_test(self, state):
        return len(state) == self.n and count_conflicts(state, self.n) == 0

    def actions(self, state):
        if len(state) == self.n:
            return []
        return list(range(self.n))

    def result(self, state, action):
        return state + (action,)

    def step_cost(self, state, action):
        return 1
    
