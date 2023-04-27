import pandas as pd

# Leer el archivo Excel
df = pd.read_excel("Datos.xlsx", sheet_name="Hoja1", usecols=["Nombre", "Correo"])

# Obtener los correos únicos
Correos = df["Correo"].drop_duplicates()

# Imprimir los correos de Datos.XLSX
for correo in Correos:
    print(correo)
