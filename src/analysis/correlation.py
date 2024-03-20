import os
import pandas as pd
from scipy.stats import pearsonr

from modelisation import modelize

# Paths vers les données
loopback_results_path = os.path.abspath("./data/results/loopbackResults.csv")
nest_results_path = os.path.abspath("./data/results/nestjsResults.csv")

# Liste des colonnes de métriques
metric_columns = [
    'Average cyclomatic complexity for classes',
    'Average cyclomatic complexity for methods',
    'Number of classes with cyclomatic complexity greater than 7',
    'Number of methods with cyclomatic complexity greater than 4',
    'Average lines by class',
    'Average lines by method',
    'Median lines of classes',
    'Median lines of methods',
    'Number of God Classes (more than 50 lines)',
    'Number of God Methods (more than 30 lines',
    'Total lines in classes',
    'Total lines in methods',
    'Proportion of commented methods (%)',
    'Proportion of commented classes (%)',
    'Average LCOM',
    'Average methods by class',
    'Total lignes de code',
    'Ratio commentaires/code'
]

# Chargement des données à partir des fichiers CSV
loopback_df = pd.read_csv(loopback_results_path)
nestjs_df = pd.read_csv(nest_results_path)

# Affichage des premières lignes de chaque DataFrame pour comprendre la structure des données
#print(loopback_df.head(), nestjs_df.head())

# Ajout d'une colonne 'Framework' à chaque DataFrame
loopback_df['Framework'] = 'LoopBack'
nestjs_df['Framework'] = 'NestJS'

# Fusion des deux DataFrames
combined_df = pd.concat([loopback_df, nestjs_df], ignore_index=True)

# Affichage des premières lignes du DataFrame combiné pour vérification 

#print(combined_df.head(), combined_df.tail())

# Transformation de la colonne 'Framework' en une variable numérique
# Assignons LoopBack à 0 et NestJS à 1
combined_df['Framework_Code'] = combined_df['Framework'].apply(lambda x: 0 if x == 'LoopBack' else 1)

# Calcul de la corrélation de Pearson pour chaque métrique par rapport au framework
correlation_results = {}

for column in metric_columns:
    print(column)
    correlation_coefficient, p_value = pearsonr(combined_df[column], combined_df['Framework_Code'])
    correlation_results[column] = {'Correlation Coefficient': correlation_coefficient, 'P-Value': p_value}

# Conversion des résultats de corrélation en DataFrame pour l'exportation
correlation_results_df = pd.DataFrame.from_dict(correlation_results, orient='index')
correlation_results_df.reset_index(inplace=True)
correlation_results_df.rename(columns={'index': 'Metric'}, inplace=True)

# Chemin du fichier CSV où les résultats seront sauvegardés
output_file_path = os.path.abspath('data/results/correlation_results.csv')

# Sauvegarde des résultats dans un fichier CSV
correlation_results_df.to_csv(output_file_path, index=False)

# Génération des visualisations
modelize(combined_df)
print('Modélisation terminé.')