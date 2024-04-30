import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

f = open("direction.txt", "r", encoding='utf8')
directionData = f.readlines()
f.close()

X_direction = []
y_direction = []

for i in range(len(directionData)-1):
    X_direction.append([float(directionData[i].split(" ")[0])])
    y_direction.append([float(directionData[i].split(" ")[1])])

X_direction = np.array(X_direction)
y_direction = np.array(y_direction).ravel()

X_radiants = np.radians(X_direction)
y_radiants = np.radians(y_direction)

plt.polar(X_radiants, y_radiants, 'bo')
plt.title("Toutes les données - Direction du vent")
plt.xlabel('Valeurs prédites - Windguru')
plt.ylabel('Valeurs réelles - Pacific Palissades')
#plt.xlim([0, 360])
#plt.ylim([0, 360])
plt.show()
"""

X_train, X_test, y_train, y_test = train_test_split(X_direction, y_direction, test_size=0.25, random_state=1)
regr = MLPRegressor(random_state=1, max_iter=500).fit(X_train, y_train)
predictions = regr.predict(X_test)
score = regr.score(X_test, y_test)

"""

#plt.plot(X_direction, y_direction, 'ro')
#plt.plot(predictions, y_test, 'bo', label='Regressor')
#plt.plot(X_test, y_test, 'go', label='Data')
#plt.title("score = {}".format(score))
#plt.xlabel('Valeurs prédites')
#plt.ylabel('Valeurs réelles')
#plt.legend()
#plt.show()

# Définissez le nombre de folds pour la validation croisée
#k_fold = KFold(n_splits=5, shuffle=True, random_state=1)
#scores = cross_val_score(regr, X_direction, y_direction, cv=k_fold, scoring='r2')  # 'r2' est le coefficient de détermination

#print("Score de la régression:", score)
#print("Scores de validation croisée:", scores)
#print("Score moyen de validation croisée:", scores.mean())