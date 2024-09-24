import pandas as pd
from calculadora import calcular_agua_cultivo 
# Crear un DataFrame vacío para almacenar la info

# rmación de los cultivos

cultivos = pd.DataFrame(columns=['Cultivo', 'Variedad', 'FechaSiembra', 'FechaCosecha', 'Rendimiento', 'Plagas', 'Enfermedades',"t.riego"])

# Agregar datos de muestra
cultivos.loc[0] = ['Maíz 56', 'Dento', '2023-05-15', '2023-10-15', 5.5, 'Huitlacoche', 'no',"miercoles"]
cultivos.loc[1] = ['Tomate', 'Cherokee', '2023-06-01', '2023-08-31', 3.2, 'no', 'no',"jueves"]
cultivos.loc[2] = ['Frijol', 'Negro', '2023-05-20', '2023-09-10', 4.8, 'no', 'no',"lunes"]

# Mostrar el DataFrame
print(cultivos)



# Calcular el rendimiento promedio de todos los cultivos
rendimiento_promedio = cultivos['Rendimiento'].mean()
print("Rendimiento promedio:", rendimiento_promedio)

# Guardar el DataFrame en un archivo CSV
cultivos.to_csv('datos_cultivos.csv', index=False) 