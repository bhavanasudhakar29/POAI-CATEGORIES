
# BAYESIAN REASONING

# 1. Define Bayesian Function

def bayesian_reasoning(prior, likelihood, false_positive):

    evidence = (likelihood * prior) + \
               (false_positive * (1 - prior))

    posterior = (likelihood * prior) / evidence

    return posterior


# 2. Medical Diagnosis
# Detect disease based on medical test

medical = bayesian_reasoning(0.01, 0.95, 0.05)


# 3. Electric Vehicle
# Detect battery fault using sensor readings

ev = bayesian_reasoning(0.10, 0.90, 0.05)


# 4. Autonomous Vehicle
# Detect obstacle using vehicle sensors

av = bayesian_reasoning(0.20, 0.95, 0.10)


# 5. Smart Manufacturing
# Predict machine failure using sensor readings

manufacturing = bayesian_reasoning(0.05, 0.90, 0.10)


# 6. Display Results

print("MEDICAL DIAGNOSIS")
print("Disease Probability:", round(medical * 100, 2), "%")

print("\nELECTRIC VEHICLE")
print("Battery Fault Probability:", round(ev * 100, 2), "%")

print("\nAUTONOMOUS VEHICLE")
print("Obstacle Probability:", round(av * 100, 2), "%")

print("\nSMART MANUFACTURING")
print("Machine Failure Probability:",
      round(manufacturing * 100, 2), "%")
