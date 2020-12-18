class FanSpeed:
    def __init__(self, min=400, max=2000):
        self.min = min
        self.max = max

    # Fuzzifier
    def slowSpeed(self, rpm):
        slowBoundary = 800
        slowLimit = 1200

        if rpm < slowBoundary:
            return 1
        elif rpm < slowLimit:
            return (slowLimit - rpm) / (slowLimit - slowBoundary)
        else:
            return 0

    def fastSpeed(self, rpm):
        fastBoundary = 1000
        fastLimit = 1400

        if rpm < fastBoundary:
            return 0
        elif rpm < fastLimit:
            return (rpm - fastBoundary) / (fastLimit - fastBoundary)
        else:
            return 1

    # Defuzzifier
    def getVerySlowDomain(self, val):
        slowBoundary = 800
        slowLimit = 1200
        return slowLimit - val * val * (slowLimit-slowBoundary)

    def getSlowDomain(self, val):
        slowBoundary = 800
        slowLimit = 1200
        return slowLimit - val * (slowLimit - slowBoundary)

    def getFastDomain(self, val):
        fastBoundary = 1000
        fastLimit = 1400
        return fastBoundary + val * (fastLimit - fastBoundary)

    def getVeryFastDomain(self, val):
        fastBoundary = 1000
        fastLimit = 1400
        return fastBoundary + val * val * (fastLimit - fastBoundary)
