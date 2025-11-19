# 1. Importar las bibliotecas necesarias
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Cargar el conjunto de datos 'penguins'
# Seaborn incluye este conjunto de datos sobre pingüinos.
penguins_df = sns.load_dataset('penguins')

# Es una buena práctica eliminar filas con datos faltantes para evitar errores en el gráfico.
penguins_df.dropna(inplace=True)

# 3. Crear una cuadrícula de facetas (FacetGrid)
# Se segmentan los datos por 'species' en columnas y 'sex' en filas.
# 'hue' añade una dimensión de color basada en la 'island'.
# 'height' y 'aspect' controlan el tamaño de cada faceta.
g = sns.FacetGrid(
    data=penguins_df,
    col='species',      # Crea columnas basadas en la especie del pingüino.
    row='sex',          # Crea filas basadas en el sexo del pingüino.
    hue='island',       # Diferencia los puntos por color según la isla de origen.
    height=4,           # Altura de cada faceta en pulgadas.
    aspect=1.2          # Relación de aspecto (ancho/alto) para hacerlas más anchas.
)

# 4. Mapear un gráfico de dispersión a la cuadrícula
# Se utiliza map() para aplicar la función sns.scatterplot a cada subconjunto de datos en la cuadrícula.
g.map(
    sns.scatterplot,
    'flipper_length_mm', # Variable para el eje X.
    'body_mass_g',       # Variable para el eje Y.
    alpha=0.8            # Transparencia para ver puntos superpuestos.
)

# 5. Personalización de la visualización
# Añadir una leyenda para la variable 'hue' (island).
g.add_legend()

# Ajustar los límites de los ejes para que sean consistentes en todas las facetas.
# Esto facilita la comparación directa entre los gráficos.
g.set(xlim=(165, 240), ylim=(2500, 6500))

# Establecer las etiquetas para los ejes X e Y de toda la cuadrícula.
g.set_axis_labels('Largo de la Aleta (mm)', 'Masa Corporal (g)')

# Establecer títulos para las filas y columnas de las facetas.
# {row_name} y {col_name} son plantillas que se reemplazan por los valores de las categorías.
g.set_titles(col_template="{col_name}", row_template="{row_name}")

# Añadir un título principal a toda la figura.
# 'y=1.02' ajusta la posición vertical del título para que no se superponga con los títulos de las facetas.
plt.suptitle('Relación Aleta-Masa por Especie, Sexo e Isla', y=1.03, fontsize=16, fontweight='bold')

# Ajustar el espaciado entre subplots para evitar solapamientos.
plt.tight_layout(rect=[0, 0, 1, 0.97])

# 6. Mostrar la visualización final
plt.show()
