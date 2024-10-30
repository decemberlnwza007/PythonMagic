import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = {
    'message': [
        'Congratulations! You have won a $1000 Walmart gift card. Go to http://spamlink.com to claim now!',
        'Hello, I hope you are doing well.',
        'Earn money fast by working from home! Click here to learn more.',
        'Your account statement is ready for download.',
        'Important: Update your account information to avoid deactivation.'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam']  
}
df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train) 

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"ความแม่นยำของโมเดล: {accuracy * 100:.2f}%")


new_message = ["Free entry in 2 a weekly competition to win a prize!"]
new_message_transformed = vectorizer.transform(new_message)
prediction = model.predict(new_message_transformed)
print(f"ผลลัพธ์การทำนายข้อความ: {prediction[0]}")
