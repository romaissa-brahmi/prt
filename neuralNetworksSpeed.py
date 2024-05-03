import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator
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
X_direction = np.array(X_direction)
X = np.hstack([X_speed, X_direction])
y_speed = np.array(y_speed).ravel()

"""
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

surf = ax.scatter(X_speed, X_direction,  y_speed, c=X_direction, cmap='viridis')
ax.set_title("Toutes les données - Vitesse et direction du vent")
ax.set_xlabel('Vitesse prédite - Windguru')
ax.set_zlabel('Direction prédite - Windguru')
ax.set_ylabel('Vitesse réelle - Pacific palissades')

# Ajouter une barre de couleur
cbar = fig.colorbar(surf)

# Calcul des limites de la barre de couleur
min_val = np.min(y_speed)
max_val = np.max(y_speed)

# Définir un intervalle plus serré pour les graduations de la colorbar
tick_values = np.linspace(min_val, max_val, num=10)  # Augmenter le nombre de points selon le besoin

# Appliquer les graduations à la colorbar
cbar.set_ticks(tick_values)
cbar.set_ticklabels([f"{val:.2f}" for val in tick_values])
ax.view_init(elev=20, azim=-90)  # Modifier ici selon vos besoins
plt.show()


def droite(X_speed, y_speed):
    regression = LinearRegression()
    regression.fit(X_speed, y_speed)
    return regression.predict(X_speed)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X_speed, X_direction, y_speed, cmap='viridis')


# droite = droite(X_speed, y_speed)
# plt.plot(X_speed, X_direction, y_speed, 'b.', label='Données')
# plt.plot(X_speed, droite, color='red', linestyle=':', label='Droite de régression')

plt.title("Toutes les données - Vitesse du vent")
plt.xlabel('Valeurs prédites - Windguru')
plt.ylabel('Valeurs réelles - Pacific Palissades')
plt.xlim([min(X_speed) - 1, max(X_speed) + 1])
plt.ylim([min(y_speed) - 1, max(y_speed) + 1])
plt.legend()
plt.show()

"""

X_train, X_test, y_train, y_test = train_test_split(X, y_speed, test_size=0.25, random_state=1)

"""
scoreS = []
i = np.linspace(10, 60, 11)
print(i)
maxScoreNeurones = 0
scoreMax = 0
for j in range(10, 61, 5):

    hidden_layer = (j,j)
    regr = MLPRegressor(hidden_layer_sizes=hidden_layer, random_state=1, max_iter=200).fit(X_train, y_train)
    predictions = regr.predict(X_test)
    score = regr.score(X_test, y_test)*100
    if scoreMax < score:
        scoreMax = score
        maxScoreNeurones = j

    scoreS.append(score)
    print("Nombres de neurones : {}, score de la régression: {:.6f}".format(j,score))



# Créer un graphique
fig, ax = plt.subplots()
print(maxScoreNeurones)
print(scoreMax)
# Tracer tous les points

# Tracer le point le plus élevé dans une couleur différente
#ax.scatter(maxScoreNeurones, scoreMax, color='red', marker='.', label='Max y_test Point')
ax.scatter(i, scoreS, color='black', marker='+')

# Tracer les lignes aux coordonnées x et y
ax.vlines(x=maxScoreNeurones, ymin=0, ymax=scoreMax, color='blue', linestyle='dashed', label='Nombre de neurones = 25 ')
ax.hlines(y=scoreMax, xmin=0, xmax=maxScoreNeurones, color='red', linestyle='dashed', label='Score = 77.25%')

# Ajouter des légendes et des titres aux axes
ax.set_xlabel('Valeurs réelles - Pacific palissades')
ax.set_ylabel('Prédiction - MLP Regressor')
plt.xlim([0, 70])
plt.ylim([min(scoreS) - 1, max(scoreS) + 1])
plt.title("Scores en fonction du nombre de neurones")
ax.legend()

# Afficher le graphique
plt.show()

"""

hidden_layer = (25,25)
regr = MLPRegressor(hidden_layer_sizes=hidden_layer, random_state=1, max_iter=200).fit(X_train, y_train)
predictions = regr.predict(X_test)
score = regr.score(X_test, y_test)*100
print("Score de la régression: {:.6f}".format(score))

coefficients = np.polyfit(y_test, predictions, 1)
pente, ordonnee_origine = coefficients
valeurs_range = np.linspace(min(y_test), max(y_test), num=100)
predictions_range = pente * valeurs_range + ordonnee_origine


fig, ax = plt.subplots(figsize=(9, 8))
ax.plot(y_test, predictions, 'b.')
ax.plot(valeurs_range, predictions_range, color='red', linestyle='--')

ax.set_xlabel('Valeurs réelles - Pacific palissades')
ax.set_ylabel('Prédiction - MLP Regressor')
ax.set_xlim([min(y_test) - 1, max(y_test) + 1])
ax.set_ylim([min(predictions) - 1, max(predictions) + 1])
ax.set_title("Données prédites par le MPL Regressor en fonction des données réelles")

# Définir explicitement les graduations des axes
ax.xaxis.set_major_locator(MaxNLocator(10))  # Augmenter pour plus de graduations sur l'axe x
ax.yaxis.set_major_locator(MaxNLocator(10))  # Augmenter pour plus de graduations sur l'axe y


plt.show()


