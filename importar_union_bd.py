import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Cargar el CSV
df = pd.read_csv("data/04_feature/union_datasets.csv", encoding="latin1")

# Conexión a MySQL
usuario = "root"
contraseña = ""
host = "localhost"
puerto = "3306"
base_de_datos = "clima_aus"

# Crear engine con SQLAlchemy
engine = create_engine(f"mysql+pymysql://{usuario}:{contraseña}@{host}:{puerto}/{base_de_datos}")

# Subir a la base de datos
df.to_sql(name="union_datasets", con=engine, index=False, if_exists="replace")

print("¡Datos insertados correctamente en MySQL!")
