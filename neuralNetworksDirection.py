import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

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

plt.plot(X_direction, y_direction, 'ro')
plt.xlabel('Valeurs prédites')
plt.ylabel('Valeurs réelles')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X_direction, y_direction, test_size=0.25, random_state=1)
regr = MLPRegressor(random_state=1, max_iter=500).fit(X_train, y_train)
predictions = regr.predict(X_test)
score = regr.score(X_test, y_test)

print(score)
