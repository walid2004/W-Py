def shortest_path(start,successors,is_goal):
    frontier=[]
    if is_goal(start):
        return (start)
    frontier.append(successors(start))
    while frontier:
        x = frontier.pop(0)
        z = x[-1]
        if is_goal(z):
            return x
        else:
            frontier.append(successors(z))

        