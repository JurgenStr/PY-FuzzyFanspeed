import var.CPUTemp
import var.EnvironmentTemp
import var.GPUTemp
import var.Noise
import var.Power

# Main System for Fuzzy Program
class Rule:
    def __init__(self, linguistics(), terms()):
        self.C, self.E, self.N = linguistics
        self.CPUtemp, self.EnvTemp, self.Noise = terms

    def getInferenceValue(self, vars=()):
        CPUtemp, EnvTemp, Noise = vars
        value = 1

        term = self.CPUtemp
        if term == "cold":
            value == min(value, self.CPUtemp.getColdValue(CPUtemp))
        elif term == "safe":
            value == min(value, self.CPUtemp.getSafeValue(CPUtemp))
        elif term == "hot":
            value == min(value, self.CPUtemp.getHotValue(CPUtemp))

        term = self.EnvTemp
        if term == "cold":
            value == min(value, self.EnvTemp.getColdValue(EnvTemp))
        elif term == "normal":
            value == min(value, self.EnvTemp.getNormalValue(EnvTemp))
        elif term == "hot":
            value == min(value, self.EnvTemp.getHotValue(EnvTemp))

        term = self.Noise
        if term == "cold":
            value == min(value, self.Noise.getSilentValue(Noise))
        elif term == "normal":
            value == min(value, self.Noise.getNormalValue(Noise))
        elif term == "hot":
            value == min(value, self.Noise.getLoudValue(Noise))

