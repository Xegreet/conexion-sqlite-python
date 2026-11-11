# Conexión SQLite con Python

Este repositorio contiene un ejemplo sencillo para crear y utilizar una base de datos SQLite desde Python.

## Respuestas

### 1. ¿Cuál es la diferencia entre una conexión MySQL/PostgreSQL y SQLite?

La principal diferencia está en la forma en que funcionan y se conectan a las bases de datos.

MySQL y PostgreSQL son sistemas de gestión de bases de datos que normalmente funcionan mediante un servidor. La base de datos se encuentra alojada en un equipo o servidor, y los programas se conectan a ella a través de una red utilizando credenciales como el usuario, la contraseña, la dirección del servidor y el nombre de la base de datos.

SQLite, por otro lado, funciona directamente mediante un archivo. No necesita un servidor independiente, ya que Python puede crear, abrir y modificar el archivo de la base de datos utilizando la biblioteca estándar `sqlite3`.

### 2. ¿Cuál es la importancia de conectar y desconectar los entornos?

Conectar y desconectar una base de datos es importante para garantizar que la información pueda consultarse, almacenarse y modificarse correctamente.

**Conectar** permite que el programa establezca comunicación con la base de datos para ejecutar operaciones como insertar registros, consultar información, actualizar datos o eliminarlos.

**Desconectar** permite cerrar correctamente la conexión cuando ya no se necesita. Esto ayuda a liberar recursos del equipo, evitar conexiones abiertas innecesariamente y reducir el riesgo de problemas durante las operaciones de almacenamiento.

## Ejecución

No se necesita instalar una dependencia externa. Con Python 3, ejecuta:

```bash
python crear_base.py
```

El programa creará el archivo `datos.sqlite3`, creará la tabla `personas`, insertará datos de ejemplo y mostrará una consulta.

## URL pública del proyecto

[Repositorio público en GitHub](https://github.com/Xegreet/conexion-sqlite-python)

La URL de GitHub permite consultar y descargar el código públicamente. SQLite no funciona como un servidor remoto mediante una URL: la aplicación debe descargar el proyecto o el archivo `.sqlite3` y abrirlo localmente.

## Archivos

- `crear_base.py`: crea la base de datos y ejecuta operaciones CRUD básicas.
- `esquema.sql`: contiene el esquema SQL de la tabla.
- `datos.sqlite3`: se genera al ejecutar el programa y se excluye del control de versiones para evitar subir datos locales.