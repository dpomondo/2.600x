import random


def drawing_without_replacement_sim(numTrials, reds=4, greens=4, draws=3):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    master_bucket = []
    for i in range(reds):
        master_bucket.append('red')
    for g in range(greens):
        master_bucket.append('green')
    results = 0
    for i in range(numTrials):
        # assuming copying is faster than initializing...
        bucket = master_bucket[:]
        red_res, green_res = 0, 0
        for j in range(draws):
            choice = bucket.pop(random.randint(0, len(bucket) - 1))
            if choice == 'red':
                red_res += 1
            else:
                green_res += 1
        # report how many one color was NEVER chosen
        if red_res == 0 or green_res == 0:
            results += 1
    return float(results) / float(numTrials)
