import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root")

mycu = mydb.cursor()

mycu.execute("create database Bikes")
mycu.execute("show databases")
for x in mycu:
    print(x)
