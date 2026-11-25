# Python and SQLite Connection Example

This beginner example downloads a sample SQLite database from this repository, opens it with Python's built-in `sqlite3` module, and prints the rows from the `personas` table.

## Requirements

- Python 3
- Internet access when running the script, to download the database
- No third-party Python packages

## Run

Clone the repository and run the script from its directory:

```bash
git clone https://github.com/Xegreet/conexion-sqlite-python.git
cd conexion-sqlite-python
python conectar_sqlite.py
```

The script downloads `datos.sqlite3` from the repository into `datos_descargados.sqlite3` beside the script. It then queries `id`, `nombre`, and `correo` from `personas`, ordered by `id`. The downloaded file is replaced each time the script runs.

## Concepts practiced

- Opening a SQLite database with `sqlite3`
- Running a basic `SELECT` query
- Managing a connection with a context manager
- Downloading a file with Python's standard library
