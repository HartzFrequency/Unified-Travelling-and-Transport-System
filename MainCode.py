import mysql.connector
UTTSdb = mysql.connector.connect(host='localhost',user='root',password='harsh')
#print(UTTSdb.connection_id)
#print to check connection establishment
cur=UTTSdb.cursor()
cur.execute("CREATE DATABASE UTTS")