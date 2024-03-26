@echo off

:: Étape 1: Installer les dépendances
pip3 install -r requirements.txt

:: Étape 2: Se déplacer dans le dossier "./pipeline/"
cd ./pipeline/

:: Étape 3: Exécuter le script python "script.py"
python ./script.py

:: Étape 4: Retourner au dossier de niveau supérieur
cd ../..

:: Étape 5: Exécuter le script python "./analysis/correlation.py"
python ./src/analysis/correlation.py

echo Toutes les tâches ont été exécutées avec succès.

:: Pause à la fin si nécessaire
pause