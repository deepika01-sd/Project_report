import random

# Knowledge base
disease_db = {
    "Common Cold": ["cough", "sneezing", "running nose", "fever"],
    "Flu": ["fever", "headache", "fatigue", "cough", "sore throat"],
    "COVID-19": ["fever", "cough", "loss of taste", "loss of smell", "breathing difficulty"],
    "Migraine": ["headache", "nausea", "sensitivity to light", "sensitivity to sound"],
    "Stomach Infection": ["stomach pain", "vomiting", "diarrhea", "fever"]
}

advice_db = {
    "Common Cold": [
        "Drink warm fluids and take steam inhalation.",
        "Rest well and avoid cold drinks."
    ],
    "Flu": [
        "Take plenty of rest and drink fluids.",
        "Consult a doctor if fever lasts more than 3 days."
    ],
    "COVID-19": [
        "⚠ Isolate yourself and get tested immediately.",
        "Monitor oxygen levels and seek medical help if breathing is difficult."
    ],
    "Migraine": [
        "Take rest in a dark, quiet room.",
        "Avoid stress and drink water to stay hydrated."
    ],
    "Stomach Infection": [
        "Drink ORS solution to prevent dehydration.",
        "Avoid oily and spicy foods until you recover."
    ]
}

def chatbot():
    print("🤖 Hello! I am your AI Medical Expert System.")
    print("⚠ Disclaimer: I am not a doctor. I only provide basic advice.")
    print("------------------------------------------------------------")

    while True:
        user_input = input("\n🧑 You (type symptoms or 'exit' to quit): ").lower()

        if user_input in ["exit", "quit", "bye"]:
            print("🤖 Thank you! Stay healthy. ❤️")
            break

        found_diseases = []
        # check each disease
        for disease, symptoms in disease_db.items():
            match_count = sum(1 for s in symptoms if s in user_input)
            if match_count >= 2:   # at least 2 symptoms match
                found_diseases.append(disease)

        if found_diseases:
            for disease in found_diseases:
                print(f"\n🤖 Based on your symptoms, you may have **{disease}**.")
                print("💡 Advice:", random.choice(advice_db[disease]))
        else:
            # fallback: check if at least one symptom is there
            for disease, symptoms in disease_db.items():
                for s in symptoms:
                    if s in user_input:
                        print(f"\n🤖 Symptom '{s}' detected. Possible condition: **{disease}**.")
                        print("💡 Advice:", random.choice(advice_db[disease]))
                        break
                else:
                    continue
                break
            else:
                print("🤖 Sorry, I couldn’t identify a condition with those symptoms. Please consult a doctor.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
