del df['Profession']

def get_top_three(row):
    sorted_chars = row.sort_values(ascending=False).index.tolist()
    return sorted_chars[:3]

df[['Top1', 'Top2', 'Top3']] = df.apply(get_top_three, axis=1, result_type='expand')

X = df[['Linguistic', 'Logical', 'Kinesthetic', 'Visual-Spatial', 'Musical', 'Interpersonal', 'Naturalist']]
y1 = df['Top1']
y2 = df['Top2']
y3 = df['Top3']

X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=42)
_, _, y2_train, y2_test = train_test_split(X, y2, test_size=0.2, random_state=42)
_, _, y3_train, y3_test = train_test_split(X, y3, test_size=0.2, random_state=42)

clf1 = RandomForestClassifier(n_estimators=100, random_state=42)
clf2 = RandomForestClassifier(n_estimators=100, random_state=42)
clf3 = RandomForestClassifier(n_estimators=100, random_state=42)

clf1.fit(X_train, y1_train)
clf2.fit(X_train, y2_train)
clf3.fit(X_train, y3_train)

y1_pred = clf1.predict(X_test)
y2_pred = clf2.predict(X_test)
y3_pred = clf3.predict(X_test)
print(y1_pred)
print(y2_pred)
print(y3_pred)
accuracy1 = accuracy_score(y1_test, y1_pred)
accuracy2 = accuracy_score(y2_test, y2_pred)
accuracy3 = accuracy_score(y3_test, y3_pred)

#Thalaiva inga accuracy romba vary aagudhu, each time when this code is executed:
print(f"Accuracy for Top 1: {accuracy1}")
print(f"Accuracy for Top 2: {accuracy2}")
print(f"Accuracy for Top 3: {accuracy3}")
