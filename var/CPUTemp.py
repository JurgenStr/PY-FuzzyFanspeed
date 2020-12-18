class CPUTemp:
    def __init__(self, min=0, max=110):
        self.min = min
        self.max = max

    # Fuzzifier
    def getColdValue(self, val):
        a = 30
        b = 40

        if val < a:
            return 1
        elif val < b:
            return (b-val)/b-a
        else:
            return 0

    def getSafeValue(self, val):
        c = 30
        d = 40
        e = 65
        f = 80

        if val < c:
            return 0
        elif val < d:
            return (val-d)/(d-c)
        elif val < e:
            return 1
        elif val < f:
            return (f-val)/(f-e)
        else:
            return 0

    def getHotValue(self, val):
        g = 75
        h = 90

        if val < g:
            return 0
        elif val < h:
            return (val-h)/(h-g)
        else:
            return 1
