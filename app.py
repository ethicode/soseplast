import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    user='django_user',
    passwd='',
    db='soseplast_db',
    unix_socket='/run/mysqld/mysqld.sock'
)
print("Connexion OK")
conn.close()
