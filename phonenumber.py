import mysql.connector
from dotenv import load_dotenv
from datetime import *

mydb = mysql.connector.connect(host="localhost",user="root",passwd="immortal",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()
clock = datetime.strftime(datetime.now(), "%H:%M:%S")
hour = clock[0] + clock[1]
if int(hour) <=12:
    print("Good morning")
elif int(hour) >12 and int(hour) <=17:
    print("Good afternoon")
else :
    print("Good evening")

def add_number():
    number = input("Enter the number: ")
    name = input("Enter the name: ")
    mycursor.execute("INSERT INTO sql_passwords.phonenumber (PersonID, phonenumber) VALUES (%s, %s)", (name, number))
    mydb.commit()
def remove_number():
    number = input("Enter the number: ")
    name = input("Enter the name: ")
    mycursor.execute("DELETE FROM sql_passwords.phonenumber WHERE PersonID = %s AND phonenumber = %s", (name, number))
    mydb.commit()
def seeList():
    mycursor.execute("SELECT * FROM sql_passwords.phonenumber")
    result = mycursor.fetchall()
    for i,x in result:
        print(i,x)
def get_number_info():
    info = input("Do you know number or name?: ")

    if info == "name":
        name = input("Enter the name: ")
        mycursor.execute("select phonenumber from sql_passwords.phonenumber where PersonID =" + "'" + name + "'")
        data_name  = mycursor.fetchone()
        for i in data_name:
            print(i)

    elif info == "number":
        number = input("Enter the number: ")
        mycursor.execute("select PersonID from sql_passwords.phonenumber where phonenumber =" + number)
        data_number = mycursor.fetchone()
        for i in data_number:
            print(i)

print("""
1. Add number
2. Remove number
3. See list
4. Get number info
""")
function_ask = input("Enter the function you want to use(F.number): ")


if function_ask == "1":
    add_number()
elif function_ask == "2":
    remove_number()
elif function_ask == "3":
    seeList()
elif function_ask == "4":
    get_number_info()
