from django.shortcuts import render
from django.views.generic import CreateView,View
from django.urls import reverse_lazy
from .models import Questions
from .forms import QuestionsForm

# Create your views here.
class Questions(CreateView):
    model = Questions
    form_class = QuestionsForm
    template_name="q.html"
    success_url = reverse_lazy('success')
    
    

def kyc_tool(request):
    return render(request, 'kyc_tool.html')
    
def success(request):
    return render(request, 'success.html')
'''
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)


n_samples = 1000  
data = {
    'Q1': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q2': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q3': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q4': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q5': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q6': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q7': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q8': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q9': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q10': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q11': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q12': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q13': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q14': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q15': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q16': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q17': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q18': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q19': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q20': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q21': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q22': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q23': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q24': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q25': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q26': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q27': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q28': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q29': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q30': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q31': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q32': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q33': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q34': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q35': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q36': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q37': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q38': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q39': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Q40': np.random.choice(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'], n_samples),
    'Target': np.random.choice([
        'Linguistic', 'Logical-Mathematical', 'Spatial', 
        'Bodily-Kinesthetic', 'Musical', 'Interpersonal', 
        'Intrapersonal', 'Naturalistic'], n_samples)
}
df = pd.DataFrame(data)

X = df.drop('Target', axis=1)
y = df['Target']


categorical_features = X.columns

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)

def generate_report(prediction):
    recommendations = {
        'Linguistic': 'Your child shows strong linguistic intelligence. Consider activities like reading, writing, storytelling, or learning new languages.',
        'Logical-Mathematical': 'Your child shows strong logical-mathematical intelligence. Consider activities like puzzles, math games, coding, or scientific experiments.',
        'Spatial': 'Your child shows strong spatial intelligence. Consider activities like drawing, painting, building with Legos, or playing video games.',
        'Bodily-Kinesthetic': 'Your child shows strong bodily-kinesthetic intelligence. Consider activities like sports, dance, acting, or hands-on crafts.',
        'Musical': 'Your child shows strong musical intelligence. Consider activities like singing, playing instruments, composing music, or dancing.',
        'Interpersonal': 'Your child shows strong interpersonal intelligence. Consider activities like group projects, team sports, leadership roles, or volunteering.',
        'Intrapersonal': 'Your child shows strong intrapersonal intelligence. Consider activities like journaling, mindfulness, personal goal setting, or self-paced learning.',
        'Naturalistic': 'Your child shows strong naturalistic intelligence. Consider activities like nature walks, gardening, animal care, or environmental projects.'
    }
    
    return recommendations[prediction]

for i, prediction in enumerate(y_pred):
    report = generate_report(prediction)
    print(f'Report for Child {i+1}: {report}')
'''