from node import Node
from problem import Problem
from actions import Actions


def negative_check(state):
    count = 0
    for i in range(0, 5):
        if state[i] < 0:
            count += 1
    if count > 0:
        return False
    else:
        return True


def wolves_check(state):
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


def solution(child, problem):
    solution_path = []
    pointer = child
    while pointer.get_state() != problem.get_initial_state():
        solution_path.append(pointer)
        pointer = pointer.parent
    return solution_path[::-1]


def breadth_first_search(problem):
    node = Node(problem.initial_state, path_cost=0)
    expansion_counter = 0
    if problem.goal_test(node.get_state()):
        return solution(node, problem), expansion_counter
    else:
        frontier = []  # Init FIFO Queue
        nodes = []
        frontier.append(node.get_state())
        nodes.append(node)
        explored = set()  # Init empty set

        while len(frontier) != 0:
            current_node = nodes.pop(0)
            current_node_state = frontier.pop(0)
            explored.add(current_node.get_state())
            expansion_counter += 1

            # process each action
            for action in problem.actions.available:
                child = child_node(problem, current_node, action)
                if negative_check(child.get_state()) and wolves_check(child.get_state()):
                    if child.get_state() not in explored or child.get_state() not in frontier:
                        if problem.goal_test(child.get_state()):
                            return solution(child, problem), expansion_counter
                        expansion_counter += 1
                        frontier.append(child.get_state())
                        nodes.append(child)


def child_node(problem, parent, action):
    child_state = problem.actions.available[action].do(parent.get_state())
    path_cost = parent.get_path_cost() + 1
    return Node(child_state, parent=parent, action=action, path_cost=path_cost)


def main():
    """test breadth first search

    Args:
        initial state
        goal state

    Returns:
        solution path
    """

    initial_state = (0, 0, 0,
                     3, 3, 1)

    goal_state = (3, 3, 1,
                  0, 0, 0)

    actions = Actions()
    problem = Problem(initial_state, goal_state, actions)

    path, nodes_expanded = breadth_first_search(problem)

    print(nodes_expanded)
    for node in path:
        print(node.get_action(), ":", node.get_state())


if __name__ == "__main__":
    main()
