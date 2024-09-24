def calcular_agua_cultivo():
  """
  Calcula la cantidad de agua necesaria para un cultivo.

  El usuario ingresa los valores.
  """
  #dibujo 
  print("^⁠_⁠^(⁠•⁠‿⁠•⁠)")
  # Obtener datos del usuario
  eto = float(input("Ingrese la evapotranspiración de referencia (mm/día): "))
  kc = float(input("Ingrese el coeficiente de cultivo: "))
  area = float(input("Ingrese el área del cultivo (m²): "))

  # Convertir mm/día a m³/día por m²
  eto_m3_dia_m2 = eto / 1000

  # Calcular la evapotranspiración del cultivo (Etc)
  etc = eto_m3_dia_m2 * kc

  # Calcular la cantidad de agua necesaria por día (m³)
  agua_necesaria_dia = etc * area

  print("La cantidad de agua necesaria por día es:", agua_necesaria_dia, "m³ de agua")

# Llamar a la función para ejecutar la calculadora
calcular_agua_cultivo()