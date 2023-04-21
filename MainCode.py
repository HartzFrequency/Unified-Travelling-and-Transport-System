import mysql.connector
import GraphicUser_InterFace.Login_page

UTTSdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='harsh',
    database='UTTS')
# cur=UTTSdb.cursor()
# s="SELECT * from users"
# cur.execute(s)
# result=cur.fetchall()
# print(result[0])

Login_page = GraphicUser_InterFace.Login_page.Login()
Login_page.mainloop()

def Check_UP():
    print("inside function")    
    
#print(UTTSdb.connection_id)
#print to check connection establishment
