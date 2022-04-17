class Problem:
    """problem

    Initial state: 
        the starting point of the problem

    Goal state:
        the desired outcome of the problem
    """

    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def get_initial_state(self):
        return self.initial_state

    def get_goal_state(self):
        return self.goal_state

    def goal_test(self, state):
        return self.goal_state == state

    def do_action(self, state):
        return f"fake action state: {state}"


def main():
    """test problem
    """

    problem = Problem("fake initial", "fake goal")
    if problem.goal_test("fake goal"):
        print("passed")
    else:
        print("failed")


if __name__ == "__main__":
    main()
