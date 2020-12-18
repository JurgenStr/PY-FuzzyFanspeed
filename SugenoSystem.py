from var.CPUTemp import CPUTemp
from var.EnvironmentTemp import EnvironmentTemp
from var.Noise import Noise
from var.FanSpeed import FanSpeed
from var.Rules import Rule

# Initiating Values
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

# Start Program
print("== CPU Fan Speed Fuzzy System ==\n")
print("Juandito Batara Kuncoro (18/427582/PA/18542)")
print("Setyawan Putra Sujana (18/427594/PA/18554)")
print("Nauval Raafi Tanuwijaya (18/430271/PA/18784)")
CPUTemperature = int(input("CPU Temperature (0 celcius - 110 celcius): "))
EnvTemperature = int(
    input("Environment Temperature (10 celcius - 40 celcius): "))
NoiseValue = int(input("Environment Noise (0 dB - 130 dB): "))
values = (CPUTemperature, EnvTemperature, NoiseValue)

# Finding Inference Values
print("Calculating values...\n")
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

print("CPU Fan Speed (400 rpm - 2000 rpm):", int(finalRPM), "rpm\n")
input("Press any key to exit...")
