from pathlib import Path
import sqlite3
from urllib.request import urlopen


URL_BASE_DATOS = (
    "https://raw.githubusercontent.com/"
    "Xegreet/conexion-sqlite-python/main/datos.sqlite3"
)
BASE_DATOS_LOCAL = Path(__file__).with_name("datos_descargados.sqlite3")


def conectar_base_de_datos() -> None:
    """Descarga la base SQLite desde GitHub y consulta sus datos."""
    with urlopen(URL_BASE_DATOS) as respuesta:
        BASE_DATOS_LOCAL.write_bytes(respuesta.read())

    with sqlite3.connect(BASE_DATOS_LOCAL) as conexion:
        personas = conexion.execute(
            "SELECT id, nombre, correo FROM personas ORDER BY id"
        ).fetchall()

    print("Personas consultadas desde la base SQLite descargada desde GitHub:")
    for persona in personas:
        print(persona)
    print("La conexión se cerró correctamente.")


if __name__ == "__main__":
    conectar_base_de_datos()
