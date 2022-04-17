class Problem:
    """problem

    Initial state: 
        the starting point of the problem

    Goal state:
        the desired outcome of the problem

    Actions:
        available actions to the problem
    """

    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def get_initial_state(self):
        return self.initial_state

    def get_goal_state(self):
        return self.goal_state

    def get_actions(self):
        return self.actions

    def goal_test(self, state):
        return self.goal_state == state


def main():
    """test problem
    """

    problem = Problem("fake initial", "fake goal", "fake actions")
    if problem.goal_test("fake goal"):
        print("passed")
    else:
        print("failed")


if __name__ == "__main__":
    main()
