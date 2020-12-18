# Pengelompokan Linguistic Variables:
## CPU Temperature
- Cold
  - < 30 Celcius        = 1
  - [30, 40] Celcius    = (40 - x) / 10
  - Others              = 0
- Safe
  - < 30 Celcius        = 0
  - [30, 40] Celcius    = (x - 30) / 10
  - [40, 65] Celcius    = 1
  - [65, 85] Celcius    = (65 - x) / 20
  - Others              = 0
- Hot
  - < 75 Celcius        = 0
  - [75, 90] Celcius    = (x - 75) / 15
  - Others              = 1
## GPU Temperature
- Low
  - < 30 Celcius        = 1
  - [30, 40] Celcius    = (40 - x) / 10
  - Others              = 0
- Normal
  - < 35 Celcius        = 0
  - [35, 45] Celcius    = (x - 35) / 10
  - [45, 55] Celcius    = 1
  - [55, 65] Celcius    = (65 - x) / 10
  - Others              = 0
- High
  - < 60 Celcius        = 0
  - [60, 80] Celcius    = (x - 60) / 20
  - Others              = 1
## Environment Temperature
- Cold
  - < 15 Celcius        = 1
  - [15, 23] Celcius    = (23 - x) / 8
  - Others              = 0
- Normal
  - < 20 Celcius        = 0
  - [20, 23] Celcius    = (x - 20) / 3
  - [23, 27] Celcius    = 1
  - [27, 30] Celcius    = (30 - x) / 3
  - Others              = 0
- Hot
  - < 27 Celcius        = 0
  - [27, 33] Celcius    = (x - 27) / 6
  - Others              = 1
## Noise
- Silent
  - < 30 dB             = 1
  - [30, 38] dB         = (38 - x) / 8
  - Others              = 0
- Normal
  - < 34 dB             = 0
  - [34, 45] dB         = (x - 34) / 11
  - [45, 50] dB         = 1
  - [50, 59] dB         = (50 - x) / 9
  - Others              = 0
- Loud
  - < 53 dB             = 0
  - [53, 65] dB         = (x - 53) / 12
  - Others              = 1
## Rules
- IF CPUTemp is ... AND GPUTemp is ... AND Noise is ... THEN FanSpeed is ...
- IF CPUTemp is ... AND GPUTemp is ... AND Noise is ... THEN FanSpeed is ...
- IF CPUTemp is ... AND GPUTemp is ... AND Noise is ... THEN FanSpeed is ...
- IF CPUTemp is ... AND GPUTemp is ... AND Noise is ... THEN FanSpeed is ...
- IF CPUTemp is ... AND GPUTemp is ... AND Noise is ... THEN FanSpeed is ...
- IF CPUTemp is ... AND GPUTemp is ... AND Noise is ... THEN FanSpeed is ...
...
## References
- Component Temperature: https://www.techcenturion.com/optimal-temperature-of-cpu-and-gpu
- Component Temp. & Env. Temp.: https://www.makeuseof.com/tag/pc-operating-temperatures-hot-hot/
- Room Noise: https://www.archtoolbox.com/materials-systems/architectural-concepts/architectural-acoustics-acceptable-room-levels.html
- Fan Speed: https://www.buildcomputers.net/power-consumption-of-pc-components.html
- Fan Speed: https://linustechtips.com/topic/702567-how-many-rpm-do-you-run-your-fans-at/