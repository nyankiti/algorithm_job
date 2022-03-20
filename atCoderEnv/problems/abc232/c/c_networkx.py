from sys import stdin
import networkx as nx

N, M = map(int, stdin.readline().split())

G1 = nx.Graph()
G2 = nx.Graph()

G1.add_nodes_from(range(N))
G2.add_nodes_from(range(N))

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    G1.add_edge(A, B)

for _ in range(M):
    C, D = map(int, stdin.readline().split())
    G2.add_edge(C, D)

if nx.is_isomorphic(G1, G2):
    print("Yes")
else:
    print("No")
