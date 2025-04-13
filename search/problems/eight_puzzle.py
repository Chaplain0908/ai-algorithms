from .search_problem import SearchProblem

class EightPuzzleProblem(SearchProblem):
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def get_start_state(self):
        return self.start_state

    def get_goal_state(self):
        return self.goal_state

    def is_goal_state(self, state):
        return state == self.goal_state

    def get_successors(self, state):
        zero_index = state.index(0)
        x, y = zero_index//3, zero_index%3
        directions = [(-1, 0, 'Up'), (1, 0, 'Down'),
                      (0, -1, 'Left'), (0, 1, 'Right')]
        successors = []
        for dx, dy, actions in directions:
            next_x, next_y = x+dx, y+dy
            next_index = next_x*3 + next_y

            if 0 <= next_index < len(self.start_state):
                # swap zero_index and next_index
                state_list = list(state)
                state_list[zero_index], state_list[next_index] = state_list[next_index], state_list[zero_index]

                new_state = tuple(state_list)
                successors.append((new_state, actions, 1))

        return successors

    def get_cost_of_actions(self, actions):
        return len(actions)