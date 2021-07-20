# para instalar la libreria para la conexion a la BD ejecutamos el siguiente comando
# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="tareas_electrica"
)

cursor = mydb.cursor()

# ---------------Consultas ------------------------

# cursor.execute("select * from technician")
# fetchall va a devolver todas las instancias que encontro en la BD y se la asignara a resultado
# resultado = cursor.fetchall()

# fetchone va a devolver solamente el primer elemento que ha encontrado
# resultado2 = cursor.fetchone()
# print(resultado2)

# ---------------Agregar --------------------------
# query = "insert into technician (nombre, cargo_t, turno) values (%s, %s, %s)"
# values = ("Luis Rotela", "Junior", "Tarde")
# cursor.execute(query, values)
# comprometomos los cambios
# mydb.commit()
# print(cursor.rowcount)


# ---------------Modificar ------------------------
# query = "update technician set turno = %s where id_tecnico = %s"
# values = ("Noche", 6)
# cursor.execute(query, values)
# mydb.commit()


# ---------------Eliminar ------------------------
# query = "delete from technician where id_tecnico = %s"
# values = (1,)
# cursor.execute(query, values)
# mydb.commit()


# ---------------Limitando los resultados ------------------------
cursor.execute("select * from technician limit 1")
resultado = cursor.fetchall()
print(resultado)
