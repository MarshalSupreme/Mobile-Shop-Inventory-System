import mysql.connector as ms
db=ms.connect(host='localhost',user='root',password='1234')
a=input('Do you want to create database and tables (Yes/No) : ')
if a.lower()=='yes':
    print('')
    c1=db.cursor()
    c1.execute('create database Mobile_Shop;')
    c1.execute('use Mobile_Shop')
    c1.execute('create table Mobile_details(SNo integer primary key, Company varchar(30), Model varchar(30), Year integer, Cost integer);')
    c1.execute('create table Mobile_specifications(SNo integer primary key, Screen varchar(10), FrontCam varchar(20), BackCam varchar(25), Display varchar(30), RAM varchar(10), ROM varchar(15), Battery varchar(20), Processor varchar(40), Software varchar(25));')
    print('Database and Tables are created')
