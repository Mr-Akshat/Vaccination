import mysql.connector
import random
import Admin
import user
import vacc
from datetime import date
import string


user.connection2()
Admin.connection1()
vacc.connection3()
#Admin.location()

db=mysql.connector.connect(host='localhost',user='root',passwd='root')

cent='\t'*5
pent='\t'*6

if db:
    print(cent,'Connection Established Succesfully\n')

mycus=db.cursor()
mycus.execute(('create database if not exists vaccin_db'))
db=mysql.connector.connect(host='localhost',user='root',passwd='root',database='vaccin_db')
print(cent,'----------------------------------------')
print(cent,'|  Welcome to Indian Vaccination Camp  |'.upper())
print(cent,'----------------------------------------')

def menu():
    print()
    print(pent,'-----------------')
    print(pent,'|1.signup       |'.upper())
    print(pent,'|2.login        |'.upper())
    print(pent,'|3.Exit         |'.upper())
    print(pent,'-----------------')
    print()
    ch=input('Enter choice: ')
    if ch=='1':
        print(pent,'-----------------')
        print(pent,'|1.signup       |')
        print(pent,'-----------------')
        print()
        user.signup()
        empt=input('Press Any Key To Continue........')
        menu()
    elif ch=='2':
        print(pent,'-----------------')
        print(pent,'|2.login        |')
        print(pent,'-----------------')
        print()
        user.login()
        Admin.captcha()
        mycus=db.cursor()
        val=vacc.vaccn_rgtr()
        if type(val)==tuple:
            sql='insert ignore into details values'+str(val)
            #print(sql)
            mycus.execute(sql)
            db.commit()
            adr=Admin.location()
            mycus.execute('create table if not exists addr(aadhar_n bigint(12), adr varchar (30), unique(aadhar_n))')
            mycus=db.cursor()
            mycus.execute('insert ignore into addr values'+str((val[2],adr)))
            db.commit()
            Admin.otp()
            print(cent,'-------------------------')
            print(cent,'|  candidate registered  |'.upper())
            print(cent,'-------------------------')
            print()
            empt=input('Press Any Key To Continue........')
            menu()
        if type(val)==str:
            mycus=db.cursor()
            sql='update details set D2="Y" where aadhar_n='+val
            mycus.execute(sql)
            db.commit()
            Admin.otp()
            print()
            print(cent,'-------------------------')
            print(cent,'|  candidate registered  |'.upper())
            print(cent,'-------------------------')
            print()
            empt=input('Press Any Key To Continue........')
            menu()
        if type(val)==int:
            
            Admin.certificate(val)
            print()
            empt=input('Press Any Key To Continue........')
            menu()
        if type(val)==list:
            print()
            empt=input('Press Any Key To Continue........')
            menu()
            
        #Admin.otp()
        print()
        empt=input('Press Any Key To Continue........')
        menu()
        
    elif ch=='3':
        print(cent,'Together, Indiw will defeat COVID-19')
        print(cent,'                                P.M. Narendra Modi')
        return    
    
    else:
        print(pent,'***Invalid choice***'.upper())
        print()
        empt=input('Press Any Key To Continue........')
        menu()
menu()

