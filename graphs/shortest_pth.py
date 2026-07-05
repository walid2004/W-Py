def shortest_path(start,successors,is_goal):
    frontier=[]
    if is_goal(start):
        return (start)
    frontier.append([[start, successor] for successor in successors(start)])
    while frontier:
        x = frontier.pop(0)
        z = x[-1]
        if is_goal(z):
            return x
        for successor in successors(z):
            y=x
            y.append(successor)
            frontier.append(y)

        