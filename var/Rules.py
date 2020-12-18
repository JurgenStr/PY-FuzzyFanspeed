class Rule:
    def __init__(self, linguisticVar, rule):
        self.CPU, self.Environment, self.Noise, self.Fan = linguisticVar
        self.CPUTerm, self.EnvTerm, self.NoiseTerm, self.FanTerm = rule

    def getCPUValue(self, minValue, CPUTemp, term):
        # 1 = Cold, 2 = Safe, 3 = Hot
        if term == 1:
            return min(minValue, self.CPU.getColdValue(CPUTemp))
        elif term == 2:
            return min(minValue, self.CPU.getSafeValue(CPUTemp))
        elif term == 3:
            return min(minValue, self.CPU.getHotValue(CPUTemp))

    def getEnvValue(self, minValue, EnvTemp, term):
        # 1 = Cold, 2 = Safe, 3 = Hot
        if term == 1:
            return min(minValue, self.Environment.getColdValue(EnvTemp))
        elif term == 2:
            return min(minValue, self.Environment.getSafeValue(EnvTemp))
        elif term == 3:
            return min(minValue, self.Environment.getHotValue(EnvTemp))

    def getNoiseValue(self, minValue, NoiseScore, term):
        # 1 = Silent, 2 = Normal, 3 = Loud
        if term == 1:
            return min(minValue, self.Noise.getSilentValue(NoiseScore))
        elif term == 2:
            return min(minValue, self.Noise.getNormalValue(NoiseScore))
        elif term == 3:
            return min(minValue, self.Noise.getLoudValue(NoiseScore))

    def getFanSpeed(self, minValue, term):
        rpm = 0
        if term == "very slow":
            rpm = self.Fan.getVerySlowRPM(minValue)
        elif term == "slow":
            rpm = self.Fan.getSlowRPM(minValue)
        elif term == "fast":
            rpm = self.Fan.getFastRPM(minValue)
        elif term == "very fast":
            rpm = self.Fan.getVeryFastRPM(minValue)
        return rpm

    def getInferenceValue(self, values):
        CPUTemp, EnvTemp, NoiseScore = values
        minValue = 1
        minValue = self.getCPUValue(minValue, CPUTemp, self.CPUTerm)
        minValue = self.getEnvValue(minValue, EnvTemp, self.EnvTerm)
        minValue = self.getNoiseValue(minValue, NoiseScore, self.NoiseTerm)
        rpm = self.getFanSpeed(minValue, self.FanTerm)
        print(minValue)
        fixedRpm = rpm * minValue
        return minValue, fixedRpm
