class Noise:
    def __init__(self, min=0, max=130):
        self.min = min
        self.max = max

    #Fuzzifier
    def getSilentValue(self, val):
        a = 30
        b = 38

        if val < a :
            return 1
        elif val < b :
            return (b-val)/b-a
        else :
            return 0

    def getNormalValue(self, val):
        c = 34
        d = 45
        e = 50
        f = 59

        if val < c :
            return 0
        elif val < d :
            return (val-d)/(d-c)
        elif val < e :
            return 1
        elif val < f :
            return (f-val)/(f-e)
        else :
            return 0

    def getLoudValue(self, val):
        g = 53
        h = 65

        if val < g :
            return 0
        elif val < h :
            return (val-h)/(h-g)
        else :
            return 1