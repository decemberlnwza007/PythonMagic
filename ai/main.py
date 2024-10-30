from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"ความแม่นยำของโมเดล: {accuracy * 100:.2f}%")

sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)
print(f"ชนิดของดอกไม้ที่ทำนายได้: {data.target_names[prediction][0]}")
