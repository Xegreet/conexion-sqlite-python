from pathlib import Path
import sqlite3

DATABASE_PATH = Path(__file__).with_name("datos.sqlite3")


def crear_base_de_datos() -> None:
    """Crea la base SQLite, inserta datos de ejemplo y realiza una consulta."""
    with sqlite3.connect(DATABASE_PATH) as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE
            )
            """
        )

        conexion.execute(
            "INSERT OR IGNORE INTO personas (nombre, correo) VALUES (?, ?)",
            ("Ana García", "ana@example.com"),
        )
        conexion.execute(
            "INSERT OR IGNORE INTO personas (nombre, correo) VALUES (?, ?)",
            ("Luis Pérez", "luis@example.com"),
        )

        personas = conexion.execute(
            "SELECT id, nombre, correo FROM personas ORDER BY id"
        ).fetchall()

    print(f"Base de datos creada en: {DATABASE_PATH}")
    print("Personas registradas:")
    for persona in personas:
        print(persona)
    print("La conexión se cerró correctamente.")


if __name__ == "__main__":
    crear_base_de_datos()
