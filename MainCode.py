import mysql.connector
UTTSdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*****',
    database='UTTS')
#print(UTTSdb.connection_id)
#print to check connection establishment
cur=UTTSdb.cursor()
s="INSERT INTO users(first_name,last_name,birth_date,phone,address,city,state) VALUES(%s,%s,%s,%s,%s,%s,%s)"

Value1=("harsh","shrivastava","2003-06-05",8109288418,"Hathi Khana Road Morar","Gwalior","MP")

cur.execute(s,VALUES)
UTTSdb.commit()