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

