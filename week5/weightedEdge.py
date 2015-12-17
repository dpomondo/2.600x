class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        # Your code here
        return self.weight

    def __str__(self):
        # Your code here
        return "{}->{} ({})".format(self.src, self.dest, self.weight)
