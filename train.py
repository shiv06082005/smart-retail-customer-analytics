import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("data/OnlineRetail.csv", encoding="latin1")

# Remove missing values
df = df.dropna(subset=["Country"])

# Create target column
df["HighValue"] = (df["UnitPrice"] > df["UnitPrice"].median()).astype(int)

# Encode Country
le = LabelEncoder()
df["Country"] = le.fit_transform(df["Country"])

# Features
X = df[["Quantity", "UnitPrice", "Country"]]
y = df["HighValue"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier()
}

best_model = None
best_accuracy = 0

for name, model in models.items():
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print(f"{name}: {acc:.4f}")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model

# Save best model
joblib.dump(best_model, "best_model.pkl")

print("\nBest Model Saved Successfully!")