from node import Node
from actions import Actions
from problem import Problem
from queue import PriorityQueue


def heuristic(current_node, goal_state):

    heuristic = 0
    for i in range(0, 2):
        heuristic += abs(goal_state[i] - current_node[i])
    return heuristic


def a_star(problem):
    node = Node(problem.initial_state, path_cost=0)
    expansion_counter = 0
    cost = heuristic(problem.initial_state, problem.goal_state)
    if problem.goal_test(node.get_state()):
        return problem.solution(node, problem), expansion_counter
    else:
        frontier = PriorityQueue()
        frontier.put((cost, problem.initial_state))
        nodes = []
        nodes.insert(0, node)

        explored = set()  # Init empty set

        while frontier:
            current_node = nodes.pop(0)
            current_node_state = frontier.get()
            explored.add(current_node.get_state())
            expansion_counter += 1

            # process each action
            for action in problem.actions.available:
                child = child_node(problem, current_node, action)
                if problem.negative_check(child.get_state()) and problem.wolves_check(child.get_state()):
                    if child.get_state() not in explored or child.get_state() not in frontier:
                        if problem.goal_test(child.get_state()):
                            return problem.solution(child, problem), expansion_counter
                        expansion_counter += 1
                        frontier.put(child.get_state())
                        nodes.insert(0, child)


def child_node(problem, parent, action):
    child_state = problem.actions.available[action].do(parent.get_state())
    path_cost = parent.get_path_cost() + 1
    return Node(child_state, parent=parent, action=action, path_cost=path_cost)


def main():
    """test a star search

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

    path, nodes_expanded = a_star(problem)
    problem.pretty_print(path, nodes_expanded)


if __name__ == "__main__":
    main()
