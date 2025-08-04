from pymysql import Connection
from connect import dbConnectionDecorator

@dbConnectionDecorator
def tryExecuteAlter(conexion: Connection, sql, params=None):
    with conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, params)
            return True
        except Exception as e:
            print(f"Error executing SQL: {e}")
            return False

@dbConnectionDecorator
def tryExecuteSelect(conexion: Connection, sql, params=None):
    with conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, params)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error executing SQL: {e}")
            return False

def insertData (rut: str, nombre: str, apellido: str, celular: int, eva3: float | str = None) -> bool:
    sql = "INSERT INTO datos (rut, nombre, apellido, celular, eva3) VALUES (%s, %s, %s, %s, %s)"
    params = (rut, nombre, apellido, celular, eva3)

    return tryExecuteAlter(sql, params)

def selectDataPerritos () -> list[dict] | None:
    sql = "SELECT * FROM PERRO"

    return tryExecuteSelect(sql)

def selectExampleData () -> list[dict] | None:
    sql = "SELECT * FROM EJEMPLO"

    return tryExecuteSelect(sql)

def selectDataDuenos () -> list[dict] | None:
    sql = "SELECT * FROM DUENO"

    return tryExecuteSelect(sql)

def editEva (rut: str, eva3: float | None) -> None | int:
    sql = "UPDATE datos SET eva3 = %s WHERE rut = %s"
    params = (eva3, rut)

    return tryExecuteAlter(sql, params)