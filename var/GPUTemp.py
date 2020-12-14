class GPUTemp:
    def __init__(self, min=20, max=90):
        self.min = min
        self.max = max

    # Fuzzifier: {Low, Normal, High}
    def lowTemperature(self, temp):
        firstT = 30
        secondT = 40

        if temp < firstT:
            return 1
        elif temp < secondT:
            return (secondT - temp) / (secondT - firstT)
        else:
            return 0

    def normalTemperature(self, temp):
        firstT = 35
        secondT = 45
        thirdT = 55
        fourthT = 65

        if temp < firstT:
            return 0
        elif temp < secondT:
            return (temp - firstT) / (secondT - firstT)
        elif temp < thirdT:
            return 1
        elif temp < fourthT:
            return (fourthT - temp) / (fourthT - thirdT)
        else:
            return 0

    def highTemperature(self, temp):
        firstT = 60
        secondT = 80

        if temp < firstT:
            return 0
        elif temp < secondT:
            return (secondT - temp) / (secondT - firstT)
        else:
            return 1
