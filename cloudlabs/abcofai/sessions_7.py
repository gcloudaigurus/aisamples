
# This program simulates a simple AI-powered diagnostic tool for a fictional disease.  
# It uses a very basic rule-based system, not a sophisticated machine learning model.
# In a real-world scenario, a machine learning model (e.g., trained on a large dataset of patient records) 
# would replace this rule-based system for much greater accuracy and robustness.

# Define symptoms and their associated probabilities for the fictional disease "Fictitia"
symptoms = {
    "fever": 0.7,  # Probability of fever given Fictitia
    "cough": 0.6,  # Probability of cough given Fictitia
    "headache": 0.5, # Probability of headache given Fictitia
    "fatigue": 0.8 # Probability of fatigue given Fictitia

}

def diagnose_fictitia(patient_symptoms):
    """
    Diagnoses Fictitia based on reported symptoms using a simple probabilistic model.
    Args:
        patient_symptoms: A list of symptoms reported by the patient.
    Returns:
        A string indicating the diagnosis probability.
    """
    probability = 1.0
    for symptom in patient_symptoms:
        if symptom in symptoms:
            probability *= symptoms[symptom]  #Multiply probabilities for each symptom
        else:
            #Handle unknown symptom (Could be improved with more sophisticated handling)
            probability *= 0.1 #Assign a low probability for unknown symptoms.

    #Very basic threshold for diagnosis.  In real life, this would be much more sophisticated.
    if probability > 0.4:
        return f"The probability of Fictitia is high: {probability:.2f}"
    else:
        return f"The probability of Fictitia is low: {probability:.2f}. Further investigation is needed."

# Get patient symptoms from the user (replace this with actual patient data input in a real application)
patient_symptoms = input("Enter patient symptoms separated by commas (e.g., fever,cough,fatigue): ").lower().split(",")
patient_symptoms = [symptom.strip() for symptom in patient_symptoms]  # Clean the input

# Perform the diagnosis
diagnosis = diagnose_fictitia(patient_symptoms)
print(diagnosis)


#Further Development notes:
# 1. Replace the rule-based system with a machine learning model (e.g., a decision tree, random forest, or neural network).
# 2. Incorporate more sophisticated probability calculations (e.g., Bayesian networks).
# 3. Include more symptoms and diseases.
# 4. Integrate with a real-world database of patient records (with appropriate privacy protections).
# 5. Add error handling and input validation.
# 6.  Implement a user interface (GUI).
# 7. Consider ethical implications and biases in the AI model.


