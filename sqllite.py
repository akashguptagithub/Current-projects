import sqlite3
##Connect to SQLite
connection = sqlite3.connect("student.db")

##Create a cursor object to insert record,create table

cursor=connection.cursor()

#Create the table 
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""
cursor.execute(table_info)

##Insert Some more Records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A')''')
cursor.execute('''Insert Into STUDENT values('Akash','Machine Learning Engineering','B')''')
cursor.execute('''Insert Into STUDENT values('Faixal','Devops','A')''')
cursor.execute('''Insert Into STUDENT values('Rishikesh','Data Science','A')''')
cursor.execute('''Insert Into STUDENT values('Hritik','Data Science','A')''')
cursor.execute('''Insert Into STUDENT values('Vikas','Data Science','A')''')

# Display ALL the Records

print("The inserted records are ")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()