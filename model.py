import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data_list = []
with open("data/dataset1.txt", encoding='utf-8') as file:
    for line in file:
        labels = line.split()[0]
        text = line[len(labels)+1:].strip()
        labels = labels.split(",")
        mask = [0 if "__label__NORMAL" in labels else 1]
        data_list.append((text, *mask))

df1 = pd.DataFrame(data_list, columns=["text", "isToxic"])
df2 = pd.read_csv('data/labeled.csv')
df2 = df2.rename(columns={'comment': 'text', 'toxic': 'isToxic'})
df = pd.concat([df1, df2], ignore_index=True)

X = df['text']
y = df['isToxic']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=300, solver='liblinear', penalty='l1', C=10)
model.fit(X_train_vectorized, y_train)

y_pred = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, y_pred)


def predict_toxicity(comment):
    comment_vectorized = vectorizer.transform([comment])
    prediction = model.predict(comment_vectorized)
    return True if prediction[0] == 1 else False


# Пример
# new_comment = "Это просто ужасно! Кто вообще мог выпустить такой брак?"
# "Видимо, делали с закрытыми глазами. Никому не рекомендую связываться с этим дерьмом!" 
# result = predict_toxicity(new_comment)
# print(f'Комментарий: "{new_comment}" - {result}')
