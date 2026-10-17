import mysql.connector
from mysql.connector import Error

conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="MiClave123",
        database="tienda"
    )

    if conexion.is_connected():
        print("¡Conexión exitosa con MySQL!")

        cursor = conexion.cursor()

        cursor.execute("SELECT DATABASE();")
        linea = cursor.fetchone()
        print(f"Conectado a la base de datos: {linea[0]}")

        cursor.execute("SELECT * FROM productos;")
        resultados = cursor.fetchall()

        print("\n--- Listado de Productos ---")

        for producto in resultados:
            print(
                f"ID: {producto[0]} | "
                f"Nombre: {producto[1]} | "
                f"Precio: ${producto[2]} | "
                f"Stock: {producto[3]}"
            )

except Error as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    if cursor is not None:
        cursor.close()

    if conexion is not None and conexion.is_connected():
        conexion.close()
        print("\nConexión cerrada correctamente.")