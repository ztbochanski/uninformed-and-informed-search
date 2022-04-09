# uninformed-and-informed-search
Reference: [Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)
## Environmental Assumptions
- Fully Observable
- Deterministic
- Sequential 
- Static 
- Discrete 
- Single-agent

## Search Problem Components
1. A state space `S`
2. An initial state `I` exists in `S`
3. A non-empty set of goal states G that are a subset of S (G is included in S) ...goal test function that tests whether a state is a goal
4. A description of the actions available in state s, actions(s).
5. A transition model describing the result of action a applied in state s: result(s,a)
6. A cost function cost(s,a,s’)which returns the non-negative one-step cost of traveling from state s to s’ by applying a.  The cost function is only defined if s’is a successor state of s.

## Graph-Search [Pseudocode](https://github.com/aimacode/aima-pseudocode/blob/master/md/Tree-Search-and-Graph-Search.md)
> other [pseudocode](https://github.com/aimacode/aima-pseudocode/tree/master/md) examples from the book.

```rb
graph_search(problem)
 frontier = initial_state_path # queue
 reached = {state: node} # hash table that's initially empty
 solution = failure
 
  while frontier is not empty and solution can possibly be improved do
  parent = some node that we choose to remove from frontier 
    
    for child in expand(parent) do
      s = child.state
     if s is not in reached or child is a cheaper path than reached[s] then
       reached[s] = child
       frontier.add(child)
        if s is a goal and child is cheaper than solution then
        solution = child
        end
      end
    end

  end
 return solution
end
```

```rb
expand(problem, parent)
  s = parent.state
 nodes = []

 for action in problem.actions(s) do
  s_prime ← problem.result(s, action)
  cost ← parent.path-cost + problem.step-cost(_s, action, s_prime)
  add node to nodes
  end

 return nodes
end
```

## Requirements
**Args**
```zsh
<initial state file> <goal state file> <mode> <output file>
```
**Mode options**
- `bfs` for breadth-first search
- `dfs` for depth-first search
- `iddfs` for iterative deepening depth-first search
- `astar` for A-Star search

## I. Uninformed Search
>no information about states except generation of successive state and recognizing a goal state.

### Breadth First Search (BFS)

### Depth First Search (DFS)

### Iterative Deepening Depth First Search (IDDFS)

## II. Informed Search
>How to make the search smarter? Determine how good a non-goal state is.

### A-Star Search ()
