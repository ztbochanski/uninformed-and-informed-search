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

    def wolves_check(self, state):
        left_bank = state[:3]
        right_bank = state[3:]

        # greater or equal wolves to chickens ratio on both banks
        if left_bank[0] >= left_bank[1] and right_bank[0] >= right_bank[1]:
            return True
        else:
            if left_bank[0] == 0 or right_bank[0] == 0:
                return True
            else:
                return False

    def negative_check(self, state):
        count = 0
        for i in range(0, 5):
            if state[i] < 0:
                count += 1
        if count > 0:
            return False
        else:
            return True

    def solution(self, child, problem):
        solution_path = []
        pointer = child
        while pointer.get_state() != problem.get_initial_state():
            solution_path.append(pointer)
            pointer = pointer.parent
        return solution_path[::-1]

    def pretty_print(self, path, nodes_expanded):
        actions = {
            "action1": "Put one chicken in the boat",
            "action2": "Put two chickens in the boat",
            "action3": "Put one wolf in the boat",
            "action4": "Put one wolf and one chicken in the boat",
            "action5": "Put two wolves in the boat"
        }

        print("\n-------------------------------------")
        print("Expanded Nodes: ", nodes_expanded)

        print("\n-------------------------------------")
        print("Successor States")
        count = 1
        for node in path:
            print(count, "Left Bank:", node.get_state()[0], "chickens,", node.get_state()[
                1], "wolf,", node.get_state()[2], "boat | Right Bank:", 3, "chickens,", 2, "wolves,", 0, "boat")
            count += 1

        print("\n-------------------------------------")
        print("Actions")
        count = 1
        for node in path:
            print(count, node.get_action(),
                  "-", actions[node.get_action()])
            count += 1


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
