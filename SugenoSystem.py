from var.CPUTemp import CPUTemp
from var.EnvironmentTemp import EnvironmentTemp
from var.Noise import Noise
from var.FanSpeed import FanSpeed
from var.Rules import Rule

CPU = CPUTemp()
Env = EnvironmentTemp()
Noise = Noise()
FanSpeed = FanSpeed()
Variables = (CPU, Env, Noise, FanSpeed)

# 1 = Cold / Silent, 2 = Safe / Normal, 3 = Hot / Loud
# Fan Speed = Very Slow, Slow, Fast, Very Fast
rules = [
    # (CPU, Environment, Noise, Fan)
    # Noise = Silent
    (1, 1, 1, "very slow"),
    (2, 1, 1, "slow"),
    (3, 1, 1, "fast"),
    (1, 2, 1, "very slow"),
    (2, 2, 1, "slow"),
    (3, 2, 1, "fast"),
    (1, 3, 1, "slow"),
    (2, 3, 1, "fast"),
    (3, 3, 1, "fast"),
    # Noise = Normal
    (1, 1, 2, "slow"),
    (2, 1, 2, "fast"),
    (3, 1, 2, "fast"),
    (1, 2, 2, "slow"),
    (2, 2, 2, "fast"),
    (3, 2, 2, "very fast"),
    (1, 3, 2, "fast"),
    (2, 3, 2, "fast"),
    (3, 3, 2, "very fast"),
    # Noise = Loud
    (1, 1, 3, "slow"),
    (2, 1, 3, "fast"),
    (3, 1, 3, "very fast"),
    (1, 2, 3, "slow"),
    (2, 2, 3, "fast"),
    (3, 2, 3, "very fast"),
    (1, 3, 3, "fast"),
    (2, 3, 3, "very fast"),
    (3, 3, 3, "very fast")
]
completeRule = []
for rule in rules:
    completeRule.append(Rule(Variables, rule))

# Init values
CPUTemperature = 35
EnvTemperature = 30
NoiseValue = 47
values = (CPUTemperature, EnvTemperature, NoiseValue)

# Inference Values
totalRPM = 0
totalMembershipValue = 0
for i in range(len(completeRule)):
    ruleMembershipValue, ruleRPM = completeRule[i].getInferenceValue(values)
    totalRPM += ruleRPM
    totalMembershipValue += ruleMembershipValue

# Get final RPM
if totalMembershipValue == 0:
    finalRPM = totalRPM
else:
    finalRPM = totalRPM / totalMembershipValue

print("Kecepatan fan: ", int(finalRPM), "rpm")
