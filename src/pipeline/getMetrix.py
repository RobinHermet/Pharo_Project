import subprocess
import os
import csv
import git
import sys

if len(sys.argv) != 2 or sys.argv[1] not in ['nestjs', 'loopbackjs']:
    print("Usage: python script.py <project_type>")
    print("Supported project types: nestjs, loopbackjs")
    sys.exit(1)

project_type = sys.argv[1]

# En fonction du type de projet, définir les chemins CSV et de clonage
if project_type == 'nestjs':
    csv_projects_path = 'projects_nestjs.csv'
    clone_path = '/clones/nestjs/'
elif project_type == 'loopbackjs':
    csv_projects_path = 'projects_loopbackjs.csv'
    clone_path = '/clones/loopbackJs/'

# Configuration des chemins
csv_projects_path = 'projects_' + project_type + '.csv'
clone_path = 'clones/' + project_type + '/'
ts2famix_path = '/path/to/ts2famix'
moose_image_directory = '~/Documents/Pharo/images/Moose Suite 10 (stable)/'
pharo_image_path = '/path/to/your/Pharo.image'
results_csv_path = './' + project_type + 'Results.csv'
modelsDir = 'modeles/' + project_type
projects = []

# Créer le répertoire des clones s'il n'existe pas
if not os.path.exists('clones'):
    os.makedirs('clones', 755)

if not os.path.exists(clone_path):
    os.chdir('clones')
    os.makedirs(project_type, 755)
    os.chdir(os.path.join(os.path.dirname(__file__)))

def clone_repository(repo_url, clone_path, repo_name):
    repo_clone_path = os.path.join(clone_path, repo_name)
    if not os.path.exists(repo_clone_path):
        # subprocess.run(['git', 'clone', repo_url, repo_clone_path])
        git.Repo.clone_from(repo_url, repo_clone_path)
        print(f'Cloné: {repo_name}')
    else:
        print(f'Déjà cloné: {repo_name}')
    return repo_clone_path

def getModelFromTs2famix(repo_name):
        # Se déplacer dans le dossier du projet
    pathToProject = 'clones/' + project_type + '/' + repo_name
    os.chdir(pathToProject)
    # Exécuter la commande ts2famix
    output_json = repo_name + "-model.json"
    if not os.path.exists(output_json):
        print(f"Exécution de ts2famix sur tsconfig.json, sortie dans {output_json}")
        subprocess.run(["ts2famix", "-i", "tsconfig.json", "-o", output_json], check=True)
    os.chdir(os.path.join(os.path.dirname(__file__)))

# def createModeleFolderIfNot():
#     os.chdir("../../../../../..")
#     os.chdir("Documents")
#     os.chdir("Pharo")
#     os.chdir("images")
#     os.chdir("Moose Suite 10 (stable)")
#     if not os.path.exists("modeles"):
#         os.makedirs('modeles', 755)
#     os.chdir(os.path.join(os.path.dirname(__file__)))

def createModeleFolderIfNot():
    os.chdir(os.path.join(os.path.dirname(__file__)))
    if not os.path.exists("modeles"):
        os.makedirs('modeles', 755)
    os.chdir('modeles')   
    if not os.path.exists(project_type):
        os.makedirs(project_type, 755)
    os.chdir(os.path.join(os.path.dirname(__file__)))


def copy_model_to_moose(repo_name):
    createModeleFolderIfNot()
    model_path = f'{clone_path}/{repo_name}/{repo_name}-model.json'  # Ajustez selon la structure de votre dossier
    destination_path = os.path.expanduser(os.path.join(modelsDir, f'{repo_name}-model.json'))
    subprocess.run(['cp', model_path, destination_path])
    print(f'Modèle copié pour {repo_name}')



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
        getModelFromTs2famix(project_name)
        copy_model_to_moose(project_name)
        
        # # Adaptez cette partie pour extraire les métriques de `results`
        # # Exemple de format attendu : {"ProjectName": project_name, "Metric1": value1, "Metric2": value2}
        # results_dict = {"ProjectName": project_name, "Metric1": "ExampleValue1", "Metric2": "ExampleValue2"}  # Exemple
        # writer.writerow(results_dict)

print("Script terminé. ")
