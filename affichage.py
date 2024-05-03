"""
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


"""
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

"""

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
"""

