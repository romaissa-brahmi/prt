import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

f = open("speed.txt", "r", encoding='utf8')
speedData = f.readlines()
f.close()

X_speed = []
y_speed = []

for i in range(len(speedData)-1):
    X_speed.append([float(speedData[i].split(" ")[0])])
    y_speed.append([float(speedData[i].split(" ")[1])])

X_speed = np.array(X_speed)
y_speed = np.array(y_speed).ravel()

"""
plt.plot(X_speed, y_speed, 'bo')
plt.title("Toutes les données - Vitesse du vent")
plt.xlabel('Valeurs prédites - Windguru')
plt.ylabel('Valeurs réelles - Pacific Palissades')
plt.xlim([0, 41])
plt.ylim([0, 25])
plt.show()
"""

X_train, X_test, y_train, y_test = train_test_split(X_speed, y_speed, test_size=0.25, random_state=1)

hidden_layer = (20, 30)

regr = MLPRegressor(hidden_layer_sizes=hidden_layer, random_state=1, max_iter=200).fit(X_train, y_train)
predictions = regr.predict(X_test)
score = regr.score(X_test, y_test)

"""
plt.plot(y_test, predictions, 'bo', label='Regressor')
#plt.title("Predictions - score = {:.5f}".format(score))
plt.xlabel('y_test')
plt.ylabel('prediction_test')
plt.xlim([0, 25])
plt.ylim([0, 25])
plt.legend()
plt.show()

print("Score de la régression: {:.5f}".format(score))
"""

k_fold = KFold(n_splits=5, shuffle=True, random_state=1)
predictions_cv = cross_val_predict(regr, X_speed, y_speed, cv=k_fold)
scores = cross_val_score(regr, X_test, y_test, cv=k_fold, scoring='r2')

plt.plot(y_test, predictions_cv, 'bo' , label='Prédictions k-fold')
plt.xlim([0, 41])
plt.ylim([0, 41])
plt.xlabel('Vraies valeurs')
plt.ylabel('Prédictions')
plt.title('Prédictions de la validation croisée k-fold')
plt.legend()
plt.show()

print("Scores de validation croisée:", scores)
print("Score moyen de validation croisée:", scores.mean())

