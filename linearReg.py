import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_predict



f = open("speed&direction.txt", "r", encoding='utf8')
data = f.readlines()
f.close()

X_speed = []
y_speed = []
X_direction = []

for i in range(len(data) - 1):
    X_speed.append([float(data[i].split(" ")[0])])
    X_direction.append([float(data[i].split(" ")[1])])
    y_speed.append([float(data[i].split(" ")[2])])


X_speed = np.array(X_speed)
X_direction = np.array(X_speed)
y_speed = np.array(y_speed).ravel()

X_train, X_test, y_train, y_test = train_test_split(X_speed, y_speed, test_size=0.25, random_state=42)

# Entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_test)
score = model.score(X_test, y_test)
print(score)
# Visualiser les résultats
plt.figure(figsize=(12, 6))

# Pour la vitesse du vent
plt.subplot(1, 2, 1)
plt.scatter(y_test, predictions, color='blue')
plt.plot([0, 25], [0, 25], color='red', linestyle='--')
plt.xlabel('Vitesse réelle')
plt.ylabel('Vitesse prédite')
plt.title('Prévision de la vitesse du vent')

plt.tight_layout()
plt.show()
