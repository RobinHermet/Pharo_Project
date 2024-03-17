import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

plots_direc = os.path.abspath('data/graphs/')

def clean_data(combined_df):
    """Nettoie les données pour la proportion de classes commentées."""
    combined_df_cleaned = combined_df.copy()
    combined_df_cleaned['Proportion of commented classes (%)'] = pd.to_numeric(combined_df_cleaned['Proportion of commented classes (%)'], errors='coerce')
    combined_df_cleaned.dropna(subset=['Proportion of commented classes (%)'], inplace=True)
    return combined_df_cleaned

def save_plot(figure, filename):
    """Enregistre la figure dans un fichier dans le répertoire spécifié."""
    # Crée le répertoire s'il n'existe pas
    if not os.path.exists(plots_direc):
        os.makedirs(plots_direc)
    
    filepath = os.path.join(plots_direc, filename)
    figure.savefig(filepath)
    plt.close(figure)  # Ferme la figure pour libérer la mémoire

def boxplot_view(combined_df, palette, metric, ax_title, y_label):
    """Génère un boxplot pour une métrique spécifique."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Framework', y=metric, data=combined_df, palette=palette)
    plt.title(ax_title)
    plt.ylabel(y_label)
    save_plot(fig, f"boxplot_{metric}.png")


def histogram_view(combined_df, palette, metric, ax_title):
    """Génère un histogramme empilé pour une métrique spécifique."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=combined_df, x=metric, hue='Framework', multiple="stack", kde=True, palette=palette)
    plt.title(ax_title)
    save_plot(fig, f"histogram_{metric}.png")

def scatterplot_view(combined_df, palette):
    """Génère un diagramme à points pour la complexité cyclomatique moyenne."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=combined_df, x='Average cyclomatic complexity for classes', y='Average cyclomatic complexity for methods', hue='Framework', style='Framework', palette=palette)
    plt.title('Diagramme à points de la complexité cyclomatique')
    save_plot(fig, f"scatter_averageCC.png")

def violinplot_view(combined_df, palette):
    """Génère un violin plot pour la complexité cyclomatique moyenne des classes."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='Framework', y='Average cyclomatic complexity for classes', data=combined_df, palette=palette)
    plt.title('Violin plot de la complexité cyclomatique moyenne pour les classes')
    save_plot(fig, f"violinplot_averageCC.png")

def barplot_view(combined_df_cleaned, palette):
    """Génère un diagramme en barres pour la proportion moyenne de classes commentées."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Framework', y='Proportion of commented classes (%)', data=combined_df_cleaned, palette=palette)
    plt.title('Proportion moyenne de classes commentées')
    save_plot(fig, f"barchart_commentedClasses.png")

def densityplot_view(combined_df_cleaned, palette):
    """Génère un diagramme de densité pour la proportion de classes commentées."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(data=combined_df_cleaned, x='Proportion of commented classes (%)', hue='Framework', fill=True, palette=palette)
    plt.title('Distribution de la proportion de classes commentées')
    save_plot(fig, f"density_commentedClasses.png")

def modelize(combined_df):
    palette = {"LoopBack": "blue", "NestJS": "red"}
    sns.set_theme(style="whitegrid")
    
    combined_df_cleaned = clean_data(combined_df)

    # Appels de fonction pour chaque type de diagramme
    boxplot_view(combined_df, palette, 'Average lines by class', 'Boxplot des lignes moyennes par classe', 'Lignes moyennes par classe')
    boxplot_view(combined_df, palette, 'Average lines by method', 'Boxplot des lignes moyennes par méthode', 'Lignes moyennes par méthode')
    histogram_view(combined_df, palette, 'Average lines by class', 'Histogramme des lignes moyennes par classe')
    histogram_view(combined_df, palette, 'Average lines by method', 'Histogramme des lignes moyennes par méthode')
    scatterplot_view(combined_df, palette)
    violinplot_view(combined_df, palette)
    barplot_view(combined_df_cleaned, palette)
    densityplot_view(combined_df_cleaned, palette)

# Exemple d'utilisation de la fonction principale
# modelize_views(combined_df)
