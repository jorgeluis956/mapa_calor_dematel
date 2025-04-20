import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Etiquetas legibles en español
factor_labels_es_legibles = [
    "F1 - Habilidades académicas", 
    "F2 - Experiencia previa", 
    "F3 - Interacción social", 
    "F4 - Presencia social",
    "F5 - Diseño del curso", 
    "F6 - Dificultad del contenido\n(course difficulty)", 
    "F7 - Carga de compromisos\n(personales/laborales)", 
    "F8 - Disponibilidad de tiempo\npara el curso", 
    "F9 - Retroalimentación oportuna\ny clara del docente", 
    "F10 - Motivación", 
    "F11 - Apoyo social", 
    "F12 - Trabajo familiar"
]

# Códigos
codes = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']

# Matriz de datos
data = [
    [0.57, 0.60, 0.70, 0.68, 0.65, 0.71, 0.63, 0.60, 0.59, 0.71, 0.57, 0.49],
    [0.67, 0.52, 0.71, 0.67, 0.63, 0.69, 0.63, 0.59, 0.57, 0.71, 0.56, 0.49],
    [0.63, 0.59, 0.60, 0.67, 0.61, 0.68, 0.59, 0.59, 0.57, 0.69, 0.56, 0.46],
    [0.64, 0.59, 0.70, 0.58, 0.62, 0.69, 0.62, 0.60, 0.58, 0.70, 0.57, 0.47],
    [0.65, 0.59, 0.71, 0.67, 0.56, 0.72, 0.63, 0.62, 0.59, 0.70, 0.57, 0.44],
    [0.62, 0.53, 0.65, 0.61, 0.61, 0.56, 0.56, 0.57, 0.52, 0.65, 0.52, 0.41],
    [0.59, 0.53, 0.63, 0.59, 0.56, 0.64, 0.49, 0.54, 0.52, 0.64, 0.51, 0.42],
    [0.56, 0.53, 0.63, 0.58, 0.57, 0.63, 0.57, 0.47, 0.50, 0.63, 0.51, 0.40],
    [0.57, 0.52, 0.64, 0.62, 0.58, 0.64, 0.56, 0.54, 0.46, 0.63, 0.51, 0.42],
    [0.62, 0.58, 0.70, 0.67, 0.61, 0.68, 0.62, 0.59, 0.58, 0.61, 0.56, 0.47],
    [0.55, 0.50, 0.59, 0.56, 0.54, 0.59, 0.54, 0.51, 0.49, 0.61, 0.42, 0.41],
    [0.43, 0.38, 0.48, 0.45, 0.39, 0.43, 0.44, 0.39, 0.37, 0.50, 0.38, 0.27]
]

# Crear el DataFrame
df = pd.DataFrame(data, index=codes, columns=codes)

# Crear el mapa de calor
plt.figure(figsize=(12, 8))
sns.heatmap(df, annot=True, fmt=".2f", cmap="YlOrRd", linewidths=.5, square=True,
            cbar_kws={'label': 'Grado de Influencia'},
            xticklabels=codes, yticklabels=factor_labels_es_legibles)
plt.title("Mapa de calor de la matriz de afectación total", fontsize=14)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# Guardar imagen
plt.savefig("Matriz_Afectacion_Calor_Espanol.png")
plt.close()
print("✅ Imagen guardada como 'Matriz_Afectacion_Calor_Espanol.png'")
