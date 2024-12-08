import mysql.connector
import io
import pandas as pd

global parentID
parentID = ""
global childrenID
childrenID = []
global childrenNames
childrenNames = []
global currentchild
currentchild = 0

# mydb = mysql.connector.connect(
#             host = "97.99.192.150",
#             user = "root",
#             passwd = "Capstone1!",
#             database = "baby_tracker"
#         )
# c = mydb.cursor()

# username = input("Username: ")
# password = input("Password: ")

# procresult = c.callproc("proc_insert_parent",(str(username),str(password),"P0"))
# print(procresult)


user = input("test")

if all(x.isspace() for x in user):
    print(1)
else:
    print(2)



