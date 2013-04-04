import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''

    def drawball(bucket):
        ball = random.choice(bucket)
        bucket.remove(ball)
        return ball

    def sameColour(balls):
        colour = balls[0]
        for ball in balls[1:]:
            if ball != colour:
                return False
        return True

    numSame = 0
    for i in range(numTrials):
        bucket = ['r','r','r','g','g','g']
        balls = [ drawball(bucket) for i in range(3) ]

        if sameColour(balls):
            numSame += 1

    return float(numSame) / numTrials

print noReplacementSimulation(10)
