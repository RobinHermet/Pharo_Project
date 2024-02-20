import subprocess
import sys
import os


def execute_pharo_script():
    # Exécutez l'image Pharo avec le script sur le modèle importé
    pharo_command = 'bash -c cd "/Users/etiennetillier/Documents/Pharo/images/Moose Suite 10 (stable)" && "/Users/etiennetillier/Documents/Pharo/vms/100-x64/Pharo.app/Contents/MacOS/Pharo" "/Users/etiennetillier/Documents/Pharo/images/Moose Suite 10 (stable)/Moose Suite 10 (stable).image" eval "/Users/etiennetillier/Documents/Pharo/scripts/GetMetrix.st"'
    # pharo_command = f'pharo {pharo_image_path} eval --save "YourPharoScriptClass new analyzeProjectNamed: \'{repo_name}\'. Smalltalk snapshot: true andQuit: true."'
    result = subprocess.run(pharo_command, shell=True, capture_output=True, text=True)

def main():
    # Chemin du dossier courant où se trouve ce script
    current_folder = os.path.dirname(os.path.realpath(__file__))
    
    # Liste des noms de projet pour lesquels exécuter le script getMetrix.py
    projects = ["nestjs", "loopbackjs"]
    
    # Boucle pour exécuter getMetrix.py pour chaque projet
    for project in projects:
        script_path = os.path.join(current_folder, "getMetrix.py")
        # Utilisation de sys.executable pour garantir l'utilisation du même interpréteur Python
        subprocess.run([sys.executable, script_path, project], check=True)
    results = execute_pharo_script()
    print("Script terminé avec succès.")


main()
