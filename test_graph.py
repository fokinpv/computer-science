from graph import Graph, BFS, DFS


def test_init_graph():
    graph = Graph()
    assert graph.is_empty()


def test_add_edge():
    graph = Graph()
    graph.add_edge(1, 2)

    assert graph._graph[1] == {2}
    assert graph._graph[2] == {1}


def test_bfs():
    graph = Graph(Graph.DIRECTED)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    assert [v for v in BFS(graph, 2)] == [2, 0, 3, 1]


def test_dfs():
    graph = Graph(Graph.DIRECTED)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    assert [v for v in DFS(graph, 2)] == [2, 0, 1, 3]


if __name__ == '__main__':
    test_init_graph()
    test_add_edge()
    test_bfs()
    test_dfs()
