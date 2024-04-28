import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

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


X_train, X_test, y_train, y_test = train_test_split(X_speed, y_speed, test_size=0.25, random_state=1)
regr = MLPRegressor(random_state=1, max_iter=500).fit(X_train, y_train)
predictions = regr.predict(X_test)
score = regr.score(X_test, y_test)


plt.plot(X_speed, y_speed, 'ro')
plt.plot(predictions, y_test, 'bo')
plt.xlabel('Valeurs prédites')
plt.ylabel('Valeurs réelles')
plt.show()
