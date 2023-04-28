import mysql.connector

UTTSdb = mysql.connector.connect(
host='localhost',
user='root',
password='harsh',
database='UTTS')
cur=UTTSdb.cursor()

def Query_LoginCheck(username,password):
    Query="SELECT * FROM users WHERE first_name = '{}' AND Password = '{}'".format(username,password)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableFlight(frm,to):
    Query="SELECT flightNo,Name,Duration,type,capacity,fare FROM flight WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableBus(frm,to):
    Query="SELECT BusID,Name,Duration,type,capacity,fare FROM Bus WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableCar(frm,to):
    Query="SELECT CarID,Name,Duration,type,capacity,fare FROM Car WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableTrain(frm,to):
    Query="SELECT PNR,Name,Duration,type,capacity,fare FROM train WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result
