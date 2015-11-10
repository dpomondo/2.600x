import random


def noReplacementSimulation(numTrials, verbose=False):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here

    def drawThree(red=3, green=3, draws=3):
        bucket = []
        count = {}
        for r in range(red):
            bucket.append('red')
        for g in range(green):
            bucket.append('green')
        if verbose:
            print("Contents of bucket:")
            print(bucket)
        for q in range(draws):
            zed = random.choice(bucket)
            zerp = bucket.pop(bucket.index(zed))
            count[zerp] = count.get(zerp, 0) + 1
        # Returns True if all three are one color
        if verbose:
            print(bucket, count)
        return draws in count.values()

    count = 0
    for i in range(numTrials):
        result = drawThree()
        if result:
            count += 1
    if verbose:
        print("Count: {} out of {} trials".format(count, numTrials))
    return count / float(numTrials)


if __name__ == '__main__':
    numTrials = 5000
    iterations = 3
    for i in range(iterations):
        print("Test number {}...".format(i))
        res = noReplacementSimulation(numTrials)
        print("\tresult: {:>10}".format(res))
