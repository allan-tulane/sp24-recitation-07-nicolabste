from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while frontier:
        current_node = frontier.pop()
        for neighbor in graph[current_node]:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result

def connected(graph):
    """ Determine if the graph is connected """
    if not graph:  # Check if the graph is empty
        return True
    start_node = next(iter(graph)) # Start from the first node available
    reached = reachable(graph, start_node)  # Use the reachable function to find reachable nodes
    return len(reached) == len(graph)  # Check if all nodes are reachable

def n_components(graph):
    """
    Calculates the number of connected components in an undirected graph.

    Args:
    graph: A dictionary representing an undirected graph where keys are nodes and values are sets of adjacent nodes.

    Returns:
    int: Number of connected components in the graph.
    """
    visited = set()  # To track visited nodes
    component_count = 0  # Counter for connected components

    for node in graph:
        if node not in visited:  # If node hasn't been visited, it's a new component
            connected_nodes = reachable(graph, node)  # Find all nodes connected to the current node
            visited.update(connected_nodes)  # Mark them as visited
            component_count += 1  # Increment the component count

    return component_count