class EnvironmentTemp:
    def __init__(self, min=10, max=40):
        self.min = min
        self.max = max

    # Fuzzifier {Cold, Safe, Hot}
    def getColdValue(self, temp):
        firstT = 15
        secondT = 23

        if (temp < firstT):
            return 1
        elif (temp < secondT):
            return (secondT - temp) / (secondT - firstT)
        else:
            return 0

    def getSafeValue(self, temp):
        firstT = 20
        secondT = 23
        thirdT = 27
        fourthT = 30

        if (temp < firstT):
            return 0
        elif (temp < secondT):
            return (temp - firstT) / (secondT - firstT)
        elif (temp < thirdT):
            return 1
        elif (temp < fourthT):
            return (fourthT - temp) / (fourthT - thirdT)
        else:
            return 0

    def getHotValue(self, temp):
        firstT = 27
        secondT = 33

        if (temp < firstT):
            return 0
        elif (temp < secondT):
            return (temp - firstT) / (secondT - firstT)
        else:
            return 1
