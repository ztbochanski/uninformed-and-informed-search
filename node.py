class Node:
    """node in search tree

    State: 
        stored state space that this node corresponds to

    Parent:
        the node in the search tree that generated this node

    Action:
        the action that was applied to the parent to generate the node

    Path cost:
        path cost from initial state to this node
    """

    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def get_path_cost(self):
        return self.path_cost

    def set_state(self, state):
        self.state = state

    def set_parent(self, parent):
        self.parent = parent

    def set_action(self, action):
        self.action = action

    def set_path_cost(self, path_cost):
        self.path_cost = path_cost


def main():
    """test node
    """

    # actions
    # 1. Put one chicken in the boat
    # 2. Put two chickens in the boat
    # 3. Put one wolf in the boat
    # 4. Put one wolf and one chicken in the boat
    # 5. Put two wolves in the boat

    node1 = Node("fake state", "fake parent", "fake action", "fake cost")
    print(node1.get_state())


if __name__ == "__main__":
    main()
