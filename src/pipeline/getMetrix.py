import subprocess
import os
import csv
import git
import sys
import platform
import shutil 

SYSTEM = platform.system()

if len(sys.argv) != 2 or sys.argv[1] not in ['nestjs', 'loopbackjs']:
    print("Usage: python script.py <project_type>")
    print("Supported project types: nestjs, loopbackjs")
    sys.exit(1)

project_type = sys.argv[1]
# successful_projects = []
# Configuration des chemins
user_home_dir = os.path.expanduser('~')
csv_project_error_path = os.path.abspath('../../data/ts2famix_errors.csv')
csv_projects_path = os.path.abspath('../../data/projects_' + project_type + '.csv')
clone_path = os.path.abspath('../../cache/clones/' + project_type) + '/'
modelsDir = os.path.abspath(user_home_dir + "/Documents/Pharo/images/Moose Suite 10 (stable)/modeles/" + project_type)
projects = []

# Créer le répertoire des clones s'il n'existe pas
if not os.path.exists('../../cache/clones/'):
    os.makedirs('../../cache/clones/', 755)

if not os.path.exists(clone_path):
    os.chdir('../../cache/clones/')
    os.makedirs(project_type, 755)
    os.chdir(os.path.join(os.path.dirname(__file__)))

def clone_repository(repo_url, clone_path, repo_name):
    repo_clone_path = os.path.join(clone_path, repo_name)
    if not os.path.exists(repo_clone_path):
        git.Repo.clone_from(repo_url, repo_clone_path)
        print(f'Cloné: {repo_name}')
    else:
        print(f'Déjà cloné: {repo_name}')
    os.chdir(os.path.join(os.path.dirname(__file__))) 
    return repo_clone_path

def log_error_to_csv(repo_name, repo_url, error_message, csv_file=csv_project_error_path):
    # Vérifier si le fichier existe déjà pour décider s'il faut ajouter les en-têtes
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Si le fichier vient d'être créé, ajouter les en-têtes
        if not file_exists:
            writer.writerow(['RepoName', 'RepoURL', 'ErrorMessage'])
        
        writer.writerow([repo_name, repo_url, error_message])

def getModelFromTs2famix(repo_name, repo_url):
    pathToProject = os.path.join(clone_path, repo_name)
    os.chdir(pathToProject)
    output_json = repo_name + "-model.json"
    if not os.path.exists(output_json):
        try:
            if SYSTEM == 'Windows':
                subprocess.run(["ts2famix", "-i", "tsconfig.json", "-o", output_json], check=True, shell=True)
            else: 
                subprocess.run(["ts2famix", "-i", "tsconfig.json", "-o", output_json], check=True)
        except subprocess.CalledProcessError as e:
            image_path = os.path.join(modelsDir, f"{repo_name}-model.json")
            print(f"Erreur lors du traitement du projet {repo_name}: {e}")
            log_error_to_csv(repo_name, repo_url, str(e))
            try:
                shutil.rmtree(pathToProject)
                print(f"Dossier du projet {repo_name} supprimé.")
            except Exception as e:
                print(f"Erreur lors de la suppression du dossier du projet {repo_name}: {e}")
            return False  # Retourne False en cas d'erreur
    return True  # Retourne True si la commande a réussi


def createModeleFolderIfNot():
    pharo_image_path = os.path.join(user_home_dir, 'Documents/Pharo/images/Moose Suite 10 (stable)')
    os.chdir(pharo_image_path)
    if not os.path.exists("modeles"):
        os.makedirs('modeles', 755)
    os.chdir("modeles")
    if not os.path.exists(project_type):
        os.makedirs(project_type, 755)
    os.chdir(os.path.join(os.path.dirname(__file__)))


def copy_model_to_moose(repo_name):
    createModeleFolderIfNot()
    model_path = os.path.abspath(clone_path + repo_name + '/' + repo_name + '-model.json')  # Ajustez selon la structure de votre dossier
    destination_path = os.path.join(modelsDir, f'{repo_name}-model.json')
    if(SYSTEM=='Windows'):
        print("Copy with W")
        subprocess.run(['copy', model_path, destination_path], shell=True)
    else : 
        subprocess.run(['cp', model_path, destination_path])
    print(f'Modèle copié pour {repo_name}')

# def updateProjectCSV():
#     with open(csv_projects_path, mode='w', newline='', encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file, delimiter=';')  # Utilisez le délimiteur ';'
#         writer.writerow(['ProjectName', 'RepoURL'])
#         for project_name, repo_url in successful_projects:
#             writer.writerow([project_name, repo_url]) 

# Préparer le fichier CSV pour les résultats
# with open(results_csv_path, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
    
# Lire les projets depuis le fichier CSV
with open(csv_projects_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        project_data = row['ProjectName;RepoURL'].split(';')
        project_name = project_data[0]
        repo_url = project_data[1]
        projects.append((project_name, repo_url))

    # Exécuter le processus pour chaque projet
    for project_name, repo_url in projects:
        clone_repository(repo_url, clone_path, project_name)
        if getModelFromTs2famix(project_name, repo_url):
            copy_model_to_moose(project_name)

print("Script terminé. ")
