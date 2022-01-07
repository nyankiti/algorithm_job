class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # adjacency list repreresentaion
        self.graph = [[] for i in range(self.V)]
        self.visited = [False for i in range(self.V)]

    # destはdestinationの略
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    # traversalをstartする位置を引数に受け取る
    def dfs_traversal(self, v):
        # recursiveを用いるのでvisitedはメンバー変数を用いる
        self.visited[v] = True
        print(v, end=" ")

        # adjはadjacencyの略
        # recur for all adacent vertices
        for adj in self.graph[v]:
            if not self.visited[adj]:
                self.dfs_traversal(adj)

    # stackによるdfsも後で実装してみる  上のdfsと探索する順番は異なるが、dfsにはなってるっぽい？
    def dfs_traversal_stack(self, start):
        stack = [start]
        visited = set()
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            yield vertex
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                stack.append(neighbor)


if __name__ == "__main__":
    graph = Graph(13)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 5)
    graph.add_edge(2, 4)
    graph.add_edge(2, 10)
    graph.add_edge(2, 5)
    graph.add_edge(2, 7)
    graph.add_edge(3, 6)
    graph.add_edge(4, 7)
    graph.add_edge(5, 2)
    graph.add_edge(5, 8)
    graph.add_edge(6, 9)
    graph.add_edge(8, 11)
    graph.add_edge(11, 12)

    graph.dfs_traversal(1)
    print(' ')
    for num in graph.dfs_traversal_stack(1):
        print(num, end=" ")
