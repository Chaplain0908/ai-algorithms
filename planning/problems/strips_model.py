'''
strips(Stanford Research Institute Problem Solver)
An action is consisted by 3 parts:
    preconditions: before take action, what condition should be satisfied
    add_effects: after take action, the effect add in state
    del_effect: after take action, the effect deleted in state
eg. precondition of action "Pick up ball" is "hand empty" and "ball on tabl"
    after action, state will add "holding ball" and delete "ball on table"
'''

class Action:
    def __init__(self, name, preconditions, add_effects, del_effects):
        self.name = name
        self.preconditions = set(preconditions)
        self.add_effects = set(add_effects)
        self.del_effects = set(del_effects)

    def is_applicable(self, state):
        """Check if action can be applied to the current state."""
        return self.preconditions.issubset(state)

    def apply(self, state):
        """Apply the action to the current state and return the new state."""
        new_state = set(state)
        new_state.difference_update(self.del_effects)
        new_state.update(self.add_effects)
        return new_state


def get_example_planning_problem():
    '''
        Return a sample planning problem defined using STRIPS logic.
        This includes the initial state, goal state, and list of actions.
    '''

    initial_state = {"At(R1)"}
    goal_state = {"At(R3)"}

    actions = [
        Action("Move(R1,R2)", ["At(R1)"], ["At(R2)"], ["At(R1)"]),
        Action("Move(R2,R3)", ["At(R2)"], ["At(R3)"], ["At(R2)"]),
        Action("Move(R3,R1)", ["At(R3)"], ["At(R1)"], ["At(R3)"])
    ]

    return initial_state, goal_state, actions