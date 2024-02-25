import subprocess
import sys
import os
import platform

SYSTEM = platform.system()

def execute_pharo_script():
    print("Starting Pharo")
    # Exécutez l'image Pharo avec le script sur le modèle importé
    # Obtenir le chemin du répertoire de l'utilisateur
    user_home_dir = os.path.expanduser('~')
    if(SYSTEM=='Windows'):
        #Ajuster avec le path windows
        pharo_vm_path = os.path.join(user_home_dir, 'Documents\\Pharo\\vms\\100-x64\\Pharo.exe')
    else: 
        pharo_vm_path = os.path.join(user_home_dir, 'Documents/Pharo/vms/100-x64/Pharo.app/Contents/MacOS/Pharo')
    # Vous pouvez maintenant construire des chemins relatifs au répertoire de l'utilisateur

    pharo_image_path = os.path.join(user_home_dir, 'Documents/Pharo/images/Moose Suite 10 (stable)')
    script_path = os.path.join(user_home_dir, 'Documents/Pharo/scripts/GetMetrix.st')

    # Construction de la commande avec les chemins
    pharo_command = f'bash -c "cd \\"{pharo_image_path}\\" && \\"{pharo_vm_path}\\" \\"{os.path.join(pharo_image_path, "Moose Suite 10 (stable).image")}\\" eval \\"{script_path}\\""'

    # Exécution de la commande
    print("Running Pharo")
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
