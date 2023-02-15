import sqlite3

conn=sqlite3.connect('PRECIO.db')
cursor_obj = conn.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
table = """ CREATE TABLE PRECIOS_DOLAR (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            COMPRA VARCHAR(9),
            VENTA VARCHAR(9),
            FECHA VARCHAR(25) ,
            LOCAL_DE_CAMBIO VARCHAR(25)
        );"""
cursor_obj.execute(table)  
#ESTA PARTE ES PARA CERRAR EL ARCHIVO DE BASE DE DATOS
conn.commit()
