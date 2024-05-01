import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

f = open("speed.txt", "r", encoding='utf8')
speedData = f.readlines()
f.close()
f = open("direction.txt", "r", encoding='utf8')
directionData = f.readlines()
f.close()

X_speed = []
y_speed = []
X_direction = []
y_direction = []

for i in range(len(speedData) - 1):
    X_speed.append([float(speedData[i].split(" ")[0])])
    y_speed.append([float(speedData[i].split(" ")[1])])

for i in range(len(directionData) - 1):
    X_direction.append([float(directionData[i].split(" ")[0])])
    y_direction.append([float(directionData[i].split(" ")[1])])

X_speed = np.array(X_speed)
y_speed = np.array(y_speed).ravel()
X_direction = np.array(X_speed)
y_direction = np.array(y_speed).ravel()


def droite(X_speed, y_speed):
    regression = LinearRegression()
    regression.fit(X_speed, y_speed)
    return regression.predict(X_speed)


X_train, X_test, y_train, y_test = train_test_split(X_speed, y_speed, test_size=0.25, random_state=1)
scoreS = []
"""
hidden_layer = (5,)
regr = MLPRegressor(hidden_layer_sizes=hidden_layer, random_state=1, max_iter=200).fit(X_train, y_train)
predictions = regr.predict(X_test)
score = regr.score(X_test, y_test)
print("score =",score)

"""
minV = 25
maxV = 30

for i in range(minV, maxV):
    print("i =", i)
    hidden_layer = (i)
    regr = MLPRegressor(hidden_layer_sizes=hidden_layer, random_state=1, max_iter=200).fit(X_train, y_train)
    predictions = regr.predict(X_test)
    score = regr.score(X_test, y_test)
    print("score =",score)
    scoreS.append(score)


valeurs_range = np.linspace(minV - 1, maxV, num=maxV - minV)
plt.plot(valeurs_range, scoreS, 'bo')
#plt.title("Toutes les données - Vitesse du vent")
#plt.xlabel('Valeurs prédites - Windguru')
#plt.ylabel('Valeurs réelles - Pacific Palissades')
plt.xlim([minV, maxV])
plt.ylim([0,1])
#plt.legend()
plt.show()
print("{} à l'indice {}".format(max(scoreS),scoreS.index(max(scoreS))))

"""



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

print("Score de la régression: {:.5f}".format(score))


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

"""
