#Training and evaluating a model
print("\n==== Accuracy,Precision and Recall =====")

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Features: [sleep_hr, water_glasses, bench_kg]
X = np.array([
    [7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],
    [6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],
    [7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],
    [7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]
])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y = (steps >= 10000).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Classification report:")
print(classification_report(y_test, y_pred, target_names=["Below 10k", "Hit 10k"]))
#Confusion Matrix
print("\n===== CONFUSION MATRIX =====")
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y = (steps >= 10000).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(f"                Predicted Below  Predicted Hit")
print(f"Actual Below    {cm[0][0]:>14}  {cm[0][1]:>14}")
print(f"Actual Hit      {cm[1][0]:>14}  {cm[1][1]:>14}")
print()
print(f"True Negatives  (correct 'Below'):  {cm[0][0]}")
print(f"False Positives (wrong 'Hit'):       {cm[0][1]}")
print(f"False Negatives (missed 'Hit'):      {cm[1][0]}")
print(f"True Positives  (correct 'Hit'):     {cm[1][1]}")

#Feature impotance
print("\n======== FEATURE IMPORTANCE =======")
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y = (steps >= 10000).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X_train, y_train)

feature_names = ["sleep_hours", "water_glasses", "bench_press_kg"]
importances = clf.feature_importances_

print("Feature importances (how much each feature contributes):")
for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
    bar = "#" * int(imp * 40)
    print(f"  {name:<18} {imp:.3f}  {bar}")

#Comparing two algorithms
print("\n====== COMPARING TWO ALGORITHMS =====")

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y = (steps >= 10000).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

models = {
    "Decision Tree":    DecisionTreeClassifier(random_state=42),
    "Random Forest":    RandomForestClassifier(n_estimators=20, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=200),
}

print("Model comparison:")
print(f"  {'Model':<30} {'Accuracy':>10}")
print(f"  {'-'*36}")
for name, model in models.items():
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"  {name:<30} {acc:>10.0%}")

#Datatest for a Jua Kali workshop
print("\n====== JUA KALI WORKSHOP DATASET =====")
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Features: [quote_kes, job_type_encoded]
# Job types: gate=0, window grills=1, door frame=2, roof sheet=3
# Label: 1 = paid, 0 = pending/unpaid
X = np.array([
    [28000,0],[14500,1],[9800,2],[32000,0],[12000,1],
    [18500,0],[11000,2],[29500,0],[8500,3],[22000,1],
    [35000,0],[7200,2],[16000,3],[31000,0],[13500,1],
    [10500,2],[24000,0],[9000,3],[27000,1],[15000,2],
])
y = np.array([1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Job payment prediction report:")
print(classification_report(y_test, y_pred, target_names=["Unpaid", "Paid"]))