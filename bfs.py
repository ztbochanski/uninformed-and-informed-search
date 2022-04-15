# function GRAPH-SEARCH(problem) returns a solution, or failure
#  frontier ← a queue initially containing one path, for the problem's initial state
#  reached ← a table of {state: node}; initially empty
#  solution ← failure
#  while frontier is not empty and solution can possibly be improved do
#    parent ← some node that we choose to remove from frontier
#    for child in EXPAND(parent) do
#      s ← child.state
#      if s is not in reached or child is a cheaper path than reached[s] then
#        reached[s] ← child
#        add child to frontier
#        if s is a goal and child is cheaper than solution then
#          solution = child
#  return solution

# function EXPAND(problem, parent) returns a list of nodes
#  s ← parent.state
#  nodes ← an empty list
#  for action in problem.actions(s) do
#    s' ← problem.result(s, action)
#    cost ← parent.path-cost + problem.step-cost(_s, action, s')
#    add node to nodes
#  return nodes

initial_state = [0, 0, 0,
                 3, 3, 1]

goal_state = [3, 3, 1,
              0, 0, 0]


def main():
    pass


if __name__ == "__main__":
    main()
