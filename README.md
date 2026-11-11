# Base de datos SQLite

## 1. ¿Cuál es la diferencia entre una conexión MySQL/PostgreSQL y SQLite?

La principal diferencia está en la forma en que funcionan y se conectan a las bases de datos.

MySQL y PostgreSQL son sistemas de gestión de bases de datos que normalmente funcionan mediante un servidor. La base de datos se encuentra alojada en un equipo o servidor, y los programas se conectan a ella a través de una red utilizando credenciales como el usuario, la contraseña, la dirección del servidor y el nombre de la base de datos.

SQLite, por otro lado, funciona directamente mediante un archivo. No necesita un servidor independiente, ya que Python puede crear, abrir y modificar el archivo de la base de datos utilizando la biblioteca `sqlite3`.

## 2. ¿Cuál es la importancia de conectar y desconectar los entornos?

Conectar y desconectar una base de datos es importante para garantizar que la información pueda consultarse, almacenarse y modificarse correctamente.

**Conectar** permite que el programa establezca comunicación con la base de datos para ejecutar operaciones como insertar registros, consultar información, actualizar datos o eliminarlos.

**Desconectar** permite cerrar correctamente la conexión cuando ya no se necesita. Esto ayuda a liberar recursos del equipo, evitar conexiones abiertas innecesariamente y reducir el riesgo de problemas durante las operaciones de almacenamiento.

## Conexión desde GitHub

Ejecuta:

```bash
python conectar_sqlite.py
```

El programa descarga la base de datos SQLite desde esta URL pública de GitHub y luego la abre localmente:

`https://raw.githubusercontent.com/Xegreet/conexion-sqlite-python/main/datos.sqlite3`