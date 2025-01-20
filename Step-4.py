# Initialize and train RandomForestClassifier
career_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
career_classifier.fit(X_known, y_known)

# Generate data to evaluate
data_to_evaluate = []
for _ in range(10000):
    responses = [random.choice(list(scoring_structure[i].keys())) for i in range(1, 29)]
    scores = score_responses_nested(responses, scoring_structure)
    data_to_evaluate.append(scores)

# Create DataFrame for evaluation data
df_to_evaluate = pd.DataFrame(data_to_evaluate)

print(df_to_evaluate)

# Predict probabilities for each profession
career_probabilities = career_classifier.predict_proba(df_to_evaluate)

# Convert probabilities to DataFrame
career_probabilities_df = pd.DataFrame(career_probabilities, columns=career_classifier.classes_)
print(career_probabilities_df*100)
