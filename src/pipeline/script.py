import csv
import shutil
import subprocess
import sys
import os
import platform

from other_metrix.line_counter import analyze_typescript_project

SYSTEM = platform.system()
user_home_dir = os.path.expanduser('~')
current_folder = os.path.dirname(os.path.realpath(__file__))
getMetrix_script_path = os.path.join(current_folder, "getMetrix.py")
errors_script_path = os.path.join(current_folder, "error.py")


def execute_pharo_script():
    print("Starting Pharo")
    # Exécutez l'image Pharo avec le script sur le modèle importé
    # Obtenir le chemin du répertoire de l'utilisateur
    if(SYSTEM=='Windows'):
        #Ajuster avec le path windows
        pharo_vm_path = os.path.join(user_home_dir, 'Documents/Pharo/vms/100-x64/Pharo.exe')
    else: 
        pharo_vm_path = os.path.join(user_home_dir, 'Documents/Pharo/vms/100-x64/Pharo.app/Contents/MacOS/Pharo')
    # Vous pouvez maintenant construire des chemins relatifs au répertoire de l'utilisateur

    pharo_image_path = os.path.join(user_home_dir, 'Documents/Pharo/images/Moose Suite 10 (stable)')
    script_path = os.path.join(user_home_dir, 'Documents/Pharo/scripts/GetMetrix.st')

    # Construction de la commande avec les chemins
    if(SYSTEM=='Windows'):
        pharo_command = f'cmd.exe /C "cd /D "{pharo_image_path}" && "{pharo_vm_path}" "{os.path.join(pharo_image_path, "Moose Suite 10 (stable).image")}" eval "{script_path}"'
    else:
        pharo_command = f'bash -c "cd \\"{pharo_image_path}\\" && \\"{pharo_vm_path}\\" \\"{os.path.join(pharo_image_path, "Moose Suite 10 (stable).image")}\\" eval \\"{script_path}\\""'

    # Exécution de la commande
    print("Running Pharo")
    # pharo_command = f'pharo {pharo_image_path} eval --save "YourPharoScriptClass new analyzeProjectNamed: \'{repo_name}\'. Smalltalk snapshot: true andQuit: true."'
    result = subprocess.run(pharo_command, shell=True, capture_output=True, text=True)

def copy_results_to_data():

    results_path = os.path.join(user_home_dir, 'Documents/Pharo/images//Moose Suite 10 (stable)/')
    results_cp_path = os.path.abspath("../../data/results/")

    if not os.path.exists(results_cp_path):
        os.makedirs(results_cp_path, 755)


    shutil.copy(os.path.join(results_path, "nestjsResults.csv"), os.path.join(results_cp_path, "nestjsResults.csv"))
    os.remove(os.path.join(results_path, "nestjsResults.csv"))

    shutil.copy(os.path.join(results_path, "loopbackResults.csv"), os.path.join(results_cp_path, "loopbackResults.csv"))
    os.remove(os.path.join(results_path, "loopbackResults.csv"))


def get_comments(results_path, projectype):
    with open(results_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)  # Charger toutes les données dans une liste

    # En-tête du CSV
    header = data[0]
    header.extend(["Total lignes de code", "Ratio commentaires/code"])

    for line in data[1:]:  # Commencer à partir de la deuxième ligne (après l'en-tête)
        repo_name = line[0].replace("-model", "")
        code_lines, comment_lines = analyze_typescript_project(os.path.abspath("../../cache/clones/" + projectype + "/" + repo_name))
        line.extend([code_lines, (comment_lines/code_lines)])

    # Écrire les données dans le fichier CSV
    with open(results_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
            

def main():
    # Chemin du dossier courant où se trouve ce script
    
    # Liste des noms de projet pour lesquels exécuter le script getMetrix.py
    projects = ["nestjs", "loopbackjs"]
    
   # Boucle pour exécuter getMetrix.py pour chaque projet
    for project in projects:
        # Utilisation de sys.executable pour garantir l'utilisation du même interpréteur Python
        subprocess.run([sys.executable, getMetrix_script_path, project], check=True)
    results = execute_pharo_script()
    subprocess.run([sys.executable, errors_script_path], check=True)
    copy_results_to_data()

    get_comments(os.path.abspath("../../data/results/loopbackResults.csv"), "loopbackjs")
    get_comments(os.path.abspath("../../data/results/nestjsResults.csv"), "nestjs")

    print("Script terminé avec succès.")


main()
