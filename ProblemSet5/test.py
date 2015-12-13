from graph import *


def main():
    g = WeightedDigraph()
    for n in ['1', '2', '3', '4']:
        g.addNode(Node(n))
    e1 = WeightedEdge(Node('1'), Node('2'), 10, 5)
    e2 = WeightedEdge(Node('1'), Node('4'), 5, 1)
    e3 = WeightedEdge(Node('2'), Node('3'), 8, 5)
    e4 = WeightedEdge(Node('4'), Node('3'), 8, 5)
    for e in [e1, e2, e3, e4]:
        g.addEdge(e)
    return g
