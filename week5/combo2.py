# Answer:
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a 
    list of which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            if (i / (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i / (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append((names[i], vals[i], weights[i]))
    return Items
