import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold


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


def droite(X_speed, y_speed):
    regression = LinearRegression()
    regression.fit(X_speed, y_speed)
    return regression.predict(X_speed)

droite = droite(X_speed, y_speed)
plt.plot(X_speed, y_speed, 'bo', label='Données')
plt.plot(X_speed, droite, color='red', linestyle='--', label='Droite de régression')
plt.title("Toutes les données - Vitesse du vent")
plt.xlabel('Valeurs prédites - Windguru')
plt.ylabel('Valeurs réelles - Pacific Palissades')
plt.xlim([min(X_speed) - 1, max(X_speed) + 1])
plt.ylim([min(y_speed) - 1, max(y_speed) + 1])
plt.legend()
plt.show()

"""

X_train, X_test, y_train, y_test = train_test_split(X_speed, y_speed, test_size=0.25, random_state=1)
scoreS = []

hidden_layer = (20, 30)
regr = MLPRegressor(hidden_layer_sizes=hidden_layer, random_state=1, max_iter=200).fit(X_train, y_train)
predictions = regr.predict(X_test)
score = regr.score(X_test, y_test)

print("Score de la régression: {:.5f}".format(score))


coefficients = np.polyfit(y_test, predictions, 1)
pente, ordonnee_origine = coefficients
valeurs_range = np.linspace(min(y_test), max(y_test), num=100)
predictions_range = pente * valeurs_range + ordonnee_origine

plt.plot(y_test, predictions, 'bo', label='Regressor')
plt.plot(valeurs_range, predictions_range, color='red', linestyle='--', label='Droite de régression')
plt.xlabel('y_test')
plt.ylabel('prediction_test')
plt.xlim([min(y_test) - 1, max(y_test) + 1])
plt.ylim([min(predictions) - 1, max(predictions) + 1])
plt.legend()
plt.show()
"""

