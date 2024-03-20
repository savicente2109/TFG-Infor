import numpy as np
import networkx as nx

G = nx.read_edgelist("ENZYMES_g102.edges", nodetype=int)

edges = [e for e in G.edges]
print(edges)
res = []

while edges != []:
    (u, v) = edges[0]
    edges = [(t, w) for (t, w) in edges if t != u and t != v and w != u and w != v]
    res.append((u, v))

print(res)
print(len(res))

sol = [0] * G.order()
for u, v in res:
    sol[u - 1] = 1
    sol[v - 1] = 1

print(sol)
print(sum(sol))

print("\n----------------------------------\n")

G = nx.read_edgelist("aves-sparrowlyon-flock-season2-unw.edges", nodetype=int)

edges = [e for e in G.edges]
#print(edges)
res = []

while edges != []:
    (u, v) = edges[0]
    edges = [(t, w) for (t, w) in edges if t != u and t != v and w != u and w != v]
    res.append((u, v))

print(res)
print(len(res))

sol = [0] * G.order()
for u, v in res:
    sol[u - 1] = 1
    sol[v - 1] = 1

print(sol)
print(sum(sol))

print("\n----------------------------------\n")

G = nx.read_edgelist("olaa.edges", nodetype=int)

edges = [e for e in G.edges]
#print(edges)
res = []

while edges != []:
    (u, v) = edges[0]
    edges = [(t, w) for (t, w) in edges if t != u and t != v and w != u and w != v]
    res.append((u, v))

#print(res)
print(len(res))

sol = [0] * G.order()
for u, v in res:
    sol[u - 1] = 1
    sol[v - 1] = 1

print(sol)
print(sum(sol))