import pandas as pd
import matplotlib.pyplot as plt

# Ruta completa al archivo CSV
file_path = r'C:\Users\Tu Papi\Desktop\Proyect Algoritmica\Combined_Dataset\Combined_Dataset.csv'

# Cargar el DataFrame desde el archivo CSV
combined_df = pd.read_csv(file_path)

# Eliminar filas con valores nulos
combined_df = combined_df.dropna()

# Define una función para extraer los valores requeridos
def extract_values(row):
    home_team = row['team'].replace(' ', '')
    away_team = row['opponent'].replace(' ', '')
    home_score = row['team_score']
    away_score = row['opponent_score']
    result = row['result']

    # Crea dos filas para cada fila original
    row1 = {
        'match': f"{home_team}_{away_team}",
        'team': home_team,
        'opponent': away_team,
        'team_score': home_score,
        'opponent_score': away_score,
        'result': result
    }
    row2 = {
        'match': f"{away_team}_{home_team}",
        'team': away_team,
        'opponent': home_team,
        'team_score': away_score,
        'opponent_score': home_score,
        'result': 'win' if result == 'loss' else 'loss' if result == 'win' else 'draw'
    }

    return [row1, row2]

# Aplica la función a cada fila del DataFrame y crea un nuevo DataFrame
new_rows = [row for _, row in combined_df.iterrows() for row in extract_values(row)]
new_df = pd.DataFrame(new_rows)

# Guarda el nuevo DataFrame en un archivo CSV
new_df.to_csv(r'C:\Users\Tu Papi\Desktop\Proyect Algoritmica\Combined_Dataset\datos_limpios_1.csv', index=False)

# Filtrar el DataFrame para un equipo específico
team_name = "Barcelona"  # Cambia esto al nombre del equipo que desees analizar
team_df = new_df[new_df['team'] == team_name]

# Crear gráficos específicos para el equipo

# 1. Distribución de resultados del equipo
team_result_counts = team_df['result'].value_counts()
team_result_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title(f'Distribución de Resultados de {team_name}')
plt.xlabel('Resultado')
plt.ylabel('Cantidad de Partidos')
plt.show()

# 2. Comparación de puntajes del equipo y sus oponentes
plt.figure(figsize=(10, 6))
plt.scatter(team_df['team_score'], team_df['opponent_score'], alpha=0.5)
plt.title(f'Comparación de Puntajes de {team_name} y sus Oponentes')
plt.xlabel('Puntaje de Equipo')
plt.ylabel('Puntaje del Oponente')
plt.show()

# Mostrar todas las columnas y filas del nuevo DataFrame
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(team_df)

# También puedes usar .head() para mostrar solo las primeras filas si el DataFrame es muy grande
print(team_df.head())
