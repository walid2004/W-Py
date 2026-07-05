def shortest_path(start,successors,is_goal):
    if is_goal(start):
        return ([start])
    frontier= [[start, successor] for successor in successors(start)]
    while frontier:
        current_path = frontier.pop(0)
        current_node = current_path[-1]
        if is_goal(current_node):
            return current_path
        for successor in successors(current_node):
            new_path = current_path + [successor]
            frontier.append(new_path)

        