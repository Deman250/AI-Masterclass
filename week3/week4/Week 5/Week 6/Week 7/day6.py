#Assigments
print("\n ====== EXERCISE 1: TRAIN A MODEL ====== ")
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
preds = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, preds):.2%}")

#Exercise 2
print("\n======= MAKE PREDICTION =====")
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier().fit(X_train, y_train)
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])
pred = model.predict(new_sample)
names = load_iris().target_names
print(f"Predicted class: {names[pred[0]]}")

#Exercise 3
print("\n====== FEATURE IMPORTANCE =======")
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = DecisionTreeClassifier().fit(X_train, y_train)
features = load_iris().feature_names
for name, imp in zip(features, model.feature_importances_):
    print(f"{name}: {imp:.3f}")

#Exercise 4
print("\n====== CHALLENGE =======")
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression(max_iter=10000).fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))
print(f"Breast cancer classifier accuracy: {acc:.2%}")

#Exercise 5
print("\n ====== TRADE APPLICATION - CONSTRUCTION PROJECT RISK ASSESSMENT ======")
def predict_delivery_risk(crew_size, days_remaining, tasks_left):
    # efficiency: tasks per worker per day needed
    efficiency = tasks_left / (crew_size * days_remaining)
    if efficiency > 1.5:
        return "High risk: not enough time or crew"
    elif efficiency > 0.8:
        return "Medium risk: tight but possible"
    else:
        return "Low risk: on track"

projects = [
    ("Westlands Office Fit-out", 3, 5, 25),
    ("Karen Tiling Contract", 4, 10, 18),
    ("Industrial Steel Doors", 2, 3, 12),
]

print("Project Risk Assessment:")
print("-" * 45)
for name, crew, days, tasks in projects:
    risk = predict_delivery_risk(crew, days, tasks)
    print(f"{name}")
    print(f"  Crew: {crew} | Days left: {days} | Tasks: {tasks}")
    print(f"  Result: {risk}")
    print()

#EXERCISE 6
print("\n ====== FARMING APPLICATION - GOAT HEALTH RISK PREDICTOR ======")
def predict_goat_health(name, weight_loss_kg, feed_drop_pct, age_years):
    risk_score = 0
    if weight_loss_kg > 3:
        risk_score += 2
    elif weight_loss_kg > 1.5:
        risk_score += 1
    if feed_drop_pct > 30:
        risk_score += 2
    elif feed_drop_pct > 15:
        risk_score += 1
    if age_years > 8:
        risk_score += 1

    if risk_score >= 4:
        return "High risk: call vet"
    elif risk_score >= 2:
        return "Medium risk: monitor closely"
    else:
        return "Low risk: healthy"

herd = [
    ("Simba",   4.2, 35, 3),
    ("Kijana",  0.5,  8, 2),
    ("Mzee",    2.1, 20, 9),
    ("Damu",    3.8, 40, 5),
    ("Furaha",  0.8, 10, 4),
]

print("Goat Health Assessment:")
print("-" * 45)
for name, wl, fd, age in herd:
    result = predict_goat_health(name, wl, fd, age)
    print(f"{name}: weight loss {wl}kg | feed drop {fd}% | age {age}yrs")
    print(f"  Assessment: {result}\n")


#CODE CHALLENGE 1
print("\n===== PROJECT DELIVERY RISK =====")

def predict_delivery_risk(crew_size, days_remaining, tasks_left):
    efficiency = tasks_left / (crew_size * days_remaining)
    if efficiency > 1.5:
        return "High risk"
    elif efficiency > 0.8:
        return "Medium risk"
    else:
        return "Low risk"

print(predict_delivery_risk(3, 5, 25))
print(predict_delivery_risk(4, 10, 18))
print(predict_delivery_risk(2, 4, 8))

#Code challenge 2
print("\n ===== THE SIMP DETECTOR ======")

def simp_alert(money_spent, texts_replied, texts_sent, date_asked, date_accepted):
    reply_rate = texts_replied / texts_sent
    date_rate = date_accepted / date_asked
    score = (reply_rate + date_rate) / 2
    if score >= 0.5:
        return "She likes you"
    if score >= 0.2:
        return "Lukewarm"
    else:
        return "You are simping"

print(simp_alert(45000, 10, 50, 10, 0))
print(simp_alert(8000, 20, 15, 4, 2))
print(simp_alert(18000, 6, 18, 5, 1))