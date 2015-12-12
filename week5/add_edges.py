#! /usr/local/bin/python3
# coding=utf-8# Write the code that adds the appropriate edges to the graph

# in this box.
cheat = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

cheat_set = set([])

for n in cheat:
    nerd = n[0] + n[2] + n[1]
    geek = n[1] + n[0] + n[2]
    # this is a graphand not a digraph, so edges in BOTH directions get added.
    # So this is a computationally intensive way to ensure we don't add in
    # double edges.
    if (geek, n) not in cheat_set:
        if (nerd, n) not in cheat_set:
            cheat_set.add((n, geek))
            cheat_set.add((n, nerd))

# the following throws errors since Edge and addEdge live elsewhere
for pair in cheat_set:
    g.addEdge(Edge(nodes[cheat.index(pair[0])], nodes[cheat.index(pair[1])]))
