def visualize_plan(initial_state, plan, actions):
    """
    Print each step in the plan, showing the state before and after each action.

    :param initial_state: set of initial predicates
    :param plan: list of action names (strings)
    :param actions: list of Action objects
    """
    state = set(initial_state)
    print("Initial State:")
    print(sorted(state))
    print("=" * 40)

    for step, action_name in enumerate(plan, 1):
        # Find corresponding action object
        action_obj = next((a for a in actions if a.name == action_name), None)
        if action_obj is None:
            print(f"[Error] Action '{action_name}' not found in actions list.")
            continue

        # Print action
        print(f"Step {step}: Apply action -> {action_obj.name}")
        print(f"  Preconditions: {sorted(action_obj.preconditions)}")
        print(f"  Effects: +{sorted(action_obj.add_effects)}  -{sorted(action_obj.del_effects)}")

        # Apply action
        state = action_obj.apply(state)

        # Print new state
        print(f"  New State: {sorted(state)}")
        print("-" * 40)

    print("Goal Reached!")
