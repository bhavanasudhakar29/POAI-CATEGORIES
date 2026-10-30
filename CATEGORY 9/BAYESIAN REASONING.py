#electric and autonomous vehicle
def bayesian_reasoning(prior, likelihood, false_positive):
    evidence = (likelihood * prior) + (false_positive * (1 - prior))
    posterior = (likelihood * prior) / evidence
    return posterior

# Electric Vehicle - Battery Fault Detection
ev = bayesian_reasoning(0.10, 0.90, 0.05)

# Autonomous Vehicle - Obstacle Detection
av = bayesian_reasoning(0.20, 0.95, 0.10)

print("ELECTRIC VEHICLE")
print("Battery Fault Probability:", round(ev * 100, 2), "%")

print("\nAUTONOMOUS VEHICLE")
print("Obstacle Detection Probability:", round(av * 100, 2), "%")

# medical diagnosis

def medical_diagnosis(prior, likelihood, false_positive):
    evidence = (likelihood * prior) + (false_positive * (1 - prior))
    posterior = (likelihood * prior) / evidence
    return posterior

result = medical_diagnosis(0.01, 0.95, 0.05)

print("Medical Diagnosis")
print("Probability of Disease:", round(result * 100, 2), "%")

# smart manufacturing

def machine_failure(prior, likelihood, false_alarm):
    evidence = (likelihood * prior) + (false_alarm * (1 - prior))
    posterior = (likelihood * prior) / evidence
    return posterior

result = machine_failure(0.05, 0.90, 0.10)

print("Smart Manufacturing")
print("Probability of Machine Failure:", round(result * 100, 2), "%")


