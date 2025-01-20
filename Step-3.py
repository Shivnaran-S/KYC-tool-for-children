import matplotlib.pyplot as plt
import seaborn as sns

def generate_report(prediction):
    recommendations = {
        'Linguistic': 'Your child shows strong linguistic intelligence. Consider activities like reading, writing, storytelling, or learning new languages.',
        'Logical': 'Your child shows strong logical-mathematical intelligence. Consider activities like puzzles, math games, coding, or scientific experiments.',
        'Visual-Spatial': 'Your child shows strong spatial intelligence. Consider activities like drawing, painting, building with Legos, or playing video games.',
        'Kinesthetic': 'Your child shows strong bodily-kinesthetic intelligence. Consider activities like sports, dance, acting, or hands-on crafts.',
        'Musical': 'Your child shows strong musical intelligence. Consider activities like singing, playing instruments, composing music, or dancing.',
        'Interpersonal': 'Your child shows strong interpersonal intelligence. Consider activities like group projects, team sports, leadership roles, or volunteering.',
        'Naturalist': 'Your child shows strong naturalistic intelligence. Consider activities like nature walks, gardening, animal care, or environmental projects.'
    }

    return recommendations[prediction]

for i, prediction in enumerate(y1_pred):
    report = generate_report(prediction)
    print(f'Report for Child {i+1}: {report}')

def plot_intelligence_distribution(y1_pred):
    intelligence_counts = pd.Series(y1_pred).value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=intelligence_counts.index, y=intelligence_counts.values)
    plt.title('Distribution of Predicted Intelligences')
    plt.xlabel('Intelligence Type')
    plt.ylabel('Count')
    plt.show()

plot_intelligence_distribution(y1_pred)
