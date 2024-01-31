

import pandas as pd

# Leer la tabla desde la página web
url = 'https://www.ejemplo.com/pagina'
dfs = pd.read_html(url)

# Obtener el DataFrame correspondiente a la tabla
tabla = dfs[0]  # Puedes ajustar el índice según la posición de la tabla en la lista

# Imprimir el DataFrame
print(tabla)
