'''
target:
define a standard interface,
any specific questions(like maze, 8-puzzle ect.) can be called by search algorithm,
once they(questions) can achieve these interface,
without modifying the logic of algorithm
'''

from abc import ABC, abstractmethod

class SearchProblem(ABC):
    @abstractmethod
    def get_start_state(self):
        """
        return start state
        type can be tuple, string,
        类型可以是 tuple、string、custom class，depends on how questions are built
        """
        pass

    @abstractmethod
    def get_goal_state(self):
        """
        return goal state
        type can be tuple, string,
        类型可以是 tuple、string、custom class，depends on how questions are built
        """
        pass

    @abstractmethod
    def is_goal_state(self, state):
        """
        judge whether it is goal state now
        input：state
        output：True / False
        """
        pass

    @abstractmethod
    def get_successors(self, state):
        """
        give a state, return all the possible successor states
        return List of (next_state, action, cost)
        eg.[((1, 2), 'Right', 1), ((0, 1), 'Up', 1)]
        """
        pass

    @abstractmethod
    def get_cost_of_actions(self, actions):
        """
        give a series of actions,
        return total cost for doing these actions.
        mainly used in A* or check the total path cost of the solution.
        """
        pass