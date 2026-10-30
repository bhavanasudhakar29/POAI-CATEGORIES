
import numpy as np

# 1. MEDICAL DIAGNOSIS

def medical_diagnosis(fever, cough):
    low_fever = max(0, min(1, (60 - fever) / 60))
    high_fever = max(0, min(1, (fever - 40) / 60))

    low_cough = max(0, min(1, (60 - cough) / 60))
    high_cough = max(0, min(1, (cough - 40) / 60))

    # Fuzzy Rules
    rule1 = min(low_fever, low_cough)
    rule2 = max(high_fever, high_cough)

    low_risk = 20
    high_risk = 90

    numerator = rule1 * low_risk + rule2 * high_risk
    denominator = rule1 + rule2

    if denominator == 0:
        return 0

    return numerator / denominator


# 2. ELECTRIC VEHICLE - BATTERY MANAGEMENT

def electric_vehicle(temp, soc):
    safe_temp = max(0, min(1, (50 - temp) / 40))
    high_temp = max(0, min(1, (temp - 30) / 30))

    low_soc = max(0, min(1, (50 - soc) / 50))
    high_soc = max(0, min(1, (soc - 50) / 50))

    # Fuzzy Rules
    rule1 = min(low_soc, safe_temp)
    rule2 = max(high_soc, high_temp)

    high_charge = 80
    low_charge = 20

    numerator = rule1 * high_charge + rule2 * low_charge
    denominator = rule1 + rule2

    if denominator == 0:
        return 0

    return numerator / denominator


# 3. AUTONOMOUS VEHICLE - OBSTACLE DETECTION

def autonomous_vehicle(distance, speed):
    near = max(0, min(1, (50 - distance) / 50))
    far = max(0, min(1, (distance - 30) / 70))

    slow = max(0, min(1, (60 - speed) / 60))
    fast = max(0, min(1, (speed - 40) / 80))

    # Fuzzy Rules
    rule1 = near
    rule2 = min(far, slow)
    rule3 = min(far, fast)

    low_speed = 10
    medium_speed = 50
    high_speed = 80

    numerator = (rule1 * low_speed +
                 rule2 * medium_speed +
                 rule3 * high_speed)

    denominator = rule1 + rule2 + rule3

    if denominator == 0:
        return 0

    return numerator / denominator


# 4. SMART MANUFACTURING - MACHINE FAILURE

def smart_manufacturing(vibration, temperature):
    low_vibration = max(0, min(1, (60 - vibration) / 60))
    high_vibration = max(0, min(1, (vibration - 40) / 60))

    low_temp = max(0, min(1, (60 - temperature) / 60))
    high_temp = max(0, min(1, (temperature - 40) / 60))

    # Fuzzy Rules
    rule1 = min(low_vibration, low_temp)
    rule2 = max(high_vibration, high_temp)

    low_risk = 20
    high_risk = 90

    numerator = rule1 * low_risk + rule2 * high_risk
    denominator = rule1 + rule2

    if denominator == 0:
        return 0

    return numerator / denominator


# 5. TEST ALL SYSTEMS

print("MEDICAL DIAGNOSIS")
print("Disease Risk:",
      round(medical_diagnosis(80, 70), 2), "%")

print("\nELECTRIC VEHICLE")
print("Charging Level:",
      round(electric_vehicle(25, 30), 2), "%")

print("\nAUTONOMOUS VEHICLE")
print("Recommended Speed:",
      round(autonomous_vehicle(20, 40), 2), "km/h")

print("\nSMART MANUFACTURING")
print("Machine Failure Risk:",
      round(smart_manufacturing(75, 80), 2), "%")
