import os

# Vous pouvez placer votre script ici pour recuperer les donnees meteorologiques.
# Ici à titre d'exemple, la date et l'heure d'execution sont insérées à la suite du fichier "out.txt"

os.system("echo Execution du script par cron : >> sortie.txt")
os.system("date >> sortie.txt")
