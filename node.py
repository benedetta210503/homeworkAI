class Node:
    """
    A class representing a node for A* algorithm.
    Attributes:
    state : the current state represented by the node
    parent : the parent node from which this node was generated.
    action : the action that was taken to reach this state from the parent
    g : the cost from the start node to this node
    h : value of the heuristic function from this node to the goal
    f : g+h
    """
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        """
            this function initializes a node.
        """
        self.state = state     
        self.parent = parent   
        self.action = action   
        self.g = g             
        self.h = h             
        self.f = g + h         

    def __lt__(self, other):
        """
            This function compares two node,the current one and  a second node basing on the
            value for the f function.
            Return:
             -)True if the current node has a value of f lower than the other node
             -)False otherwise
        """
        return self.f < other.f
