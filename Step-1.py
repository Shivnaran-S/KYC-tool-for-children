import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Function to score responses based on the provided structure
def score_responses_nested(responses, scoring_structure):
    scores = {'Linguistic': 0, 'Logical': 0, 'Kinesthetic': 0, 'Visual-Spatial': 0, 'Musical': 0, 'Interpersonal': 0, 'Naturalist': 0}
    for i, response in enumerate(responses, 1):
        if i in scoring_structure and response in scoring_structure[i]:
            for intelligence, points in scoring_structure[i][response].items():
                scores[intelligence] += points
    return scores

# Function to generate responses based on scoring structure and mandatory intelligences
def generate_responses(scoring_structure, mandatory_intelligences):
    responses = []
    for i in range(1, 29):
        valid_responses = [response for response, impacts in scoring_structure[i].items() if any(intelligence in impacts for intelligence in mandatory_intelligences)]
        if valid_responses:
            if i <= 9:
                responses.append(random.choice(valid_responses))
            elif i <= 13:
                responses.append(random.choice(['Yes']))
            elif i <= 24:
                responses.append(random.choice(['a','b']))
            else:
                responses.append(random.choice(['a','b']))
        else:
            if i <= 9:
                responses.append(random.choice(list(scoring_structure[i].keys())))
            elif i <= 13:
                responses.append(random.choice(['No', 'Maybe']))
            elif i <= 24:
                responses.append(random.choice(['a', 'b']))
            else:
                responses.append(random.choice(['c', 'b']))
    return responses

# Define scoring structure
scoring_structure = {
    1: {'a': {'Linguistic': 1}, 'b': {'Logical': 1}, 'c': {'Visual-Spatial': 1}, 'd': {'Kinesthetic': 1}},
    2: {'a': {'Linguistic': 1}, 'b': {'Visual-Spatial': 1}},
    3: {'a': {'Linguistic': 1}, 'b': {'Logical': 1}, 'c': {'Visual-Spatial': 1}},
    4: {'a': {'Logical': 1}, 'b': {'Kinesthetic': 1}},
    5: {'a': {'Linguistic': 1}, 'b': {'Logical': 1}, 'c': {'Kinesthetic': 1}},
    6: {'a': {'Linguistic': 1}, 'b': {'Logical': 1}, 'c': {'Visual-Spatial': 1}},
    7: {'a': {'Linguistic': 1}, 'b': {'Logical': 1}, 'c': {'Kinesthetic': 1}, 'd': {'Visual-Spatial': 1}},
    8: {'a': {'Linguistic': 1}, 'b': {'Logical': 1}},
    9: {'a': {'Linguistic': 1}, 'b': {'Logical': 1}, 'c': {'Kinesthetic': 1}},
    10: {'Yes': {'Musical': 2}, 'No': {'Musical': 0}, 'Maybe': {'Musical': 1}},
    11: {'Yes': {'Musical': 2}, 'No': {'Musical': 0}, 'Maybe': {'Musical': 1}},
    12: {'Yes': {'Musical': 2}, 'No': {'Musical': 0}, 'Maybe': {'Musical': 1}},
    13: {'Yes': {'Musical': 2}, 'No': {'Musical': 0}, 'Maybe': {'Musical': 1}},
    14: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    15: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    16: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    17: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    18: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    19: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    20: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    21: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    22: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    23: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    24: {'a': {'Interpersonal': 1}, 'b': {'Interpersonal': 0}},
    25: {'a': {'Naturalist': 2}, 'b': {'Naturalist': 1}, 'c': {'Naturalist': 0}},
    26: {'a': {'Naturalist': 2}, 'b': {'Naturalist': 1}, 'c': {'Naturalist': 0}},
    27: {'a': {'Naturalist': 2}, 'b': {'Naturalist': 1}, 'c': {'Naturalist': 0}},
    28: {'a': {'Naturalist': 2}, 'b': {'Naturalist': 1}, 'c': {'Naturalist': 0}}
}

# Define professions and their mandatory intelligences
professions_intelligences = {
    'Doctor': ['Logical', 'Interpersonal', 'Kinesthetic'],
    'Civil Engineer': ['Logical', 'Visual-Spatial'],
    'Software Engineer': ['Logical', 'Visual-Spatial'],
    'Teacher': ['Linguistic', 'Interpersonal','Logical'],
    #'Artist': ['Visual-Spatial'],
    #'Musician': ['Musical','Linguistic'],
    'Writer': ['Linguistic','Interpersonal'],
    'Athlete': ['Kinesthetic'],
    'Counselor': ['Interpersonal','Linguistic'],
    #'Scientist': ['Logical', 'Naturalist'],
    'Chef': ['Kinesthetic', 'Interpersonal'],
    'Architect': ['Visual-Spatial', 'Logical'],
    #'Entrepreneur': ['Logical', 'Interpersonal'],
    'Gardener': ['Naturalist','Kinesthetic'],
    'Actor': ['Kinesthetic', 'Interpersonal']
}

# Generate data
data = []
num_samples_per_profession = 1000

for profession, intelligences in professions_intelligences.items():
    for _ in range(num_samples_per_profession):
        responses = generate_responses(scoring_structure, intelligences)
        scores = score_responses_nested(responses, scoring_structure)
        row = {
            'Profession': profession,
            'Linguistic': scores['Linguistic'],
            'Logical': scores['Logical'],
            'Kinesthetic': scores['Kinesthetic'],
            'Visual-Spatial': scores['Visual-Spatial'],
            'Musical': scores['Musical'],
            'Interpersonal': scores['Interpersonal'],
            'Naturalist': scores['Naturalist']
        }
        data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Split data into X (features) and y (target)
X_known = df[['Linguistic', 'Logical', 'Kinesthetic', 'Visual-Spatial', 'Musical', 'Interpersonal', 'Naturalist']]
y_known = df['Profession']
