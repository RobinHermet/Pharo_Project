import csv
import os

user_home_dir = os.path.expanduser('~')
pharo_errors_path = os.path.join(user_home_dir, 'Documents/Pharo/images/Moose Suite 10 (stable)/pharoError.csv')

def merge_error_files(pharo_error_file, ts2famix_error_file, nestProjects, loopbackProjects, merged_error_file):
    # Lire les informations des projets pour associer les erreurs avec les URL GitHub
    projects_info = {}
    with open(nestProjects, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # Supposons que la colonne contenant le nom du projet soit 'ProjectName'
            # et la colonne contenant l'URL GitHub soit 'RepoURL'
            projects_info[row['ProjectName']] = row['RepoURL']

    with open(loopbackProjects, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # Supposons que la colonne contenant le nom du projet soit 'ProjectName'
            # et la colonne contenant l'URL GitHub soit 'RepoURL'
            projects_info[row['ProjectName']] = row['RepoURL']

    # Lire les erreurs Pharo
    pharo_errors = {}
    with open(pharo_error_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Supposons que le modèle JSON soit nommé de façon similaire au ProjectName dans projects_info
            project_name = row['Projet'].replace('-model.json', '')
            pharo_errors[project_name] = row['Error']

    # Lire les erreurs ts2famix
    ts2famix_errors = {}
    with open(ts2famix_error_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            ts2famix_errors[row['RepoName']] = row['ErrorMessage']

    # Écrire le fichier CSV fusionné
    with open(merged_error_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['ProjectName', 'RepoURL', 'ts2famixError', 'PharoError']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for project_name, repo_url in projects_info.items():
            writer.writerow({
                'ProjectName': project_name,
                'RepoURL': repo_url,
                'ts2famixError': ts2famix_errors.get(project_name, ''),
                'PharoError': pharo_errors.get(project_name, '')
            })

# Utilisez cette fonction à la fin de votre script principal.
merge_error_files(
    pharo_error_file=pharo_errors_path,
    ts2famix_error_file='../../data/ts2famix_errors.csv',
    nestProjects='../../data/projects_nestjs.csv',
    loopbackProjects='../../data/projects_loopbackjs.csv',
    merged_error_file='../../data/merged_errors.csv'
)
