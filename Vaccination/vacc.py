import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='root',database='vaccin_db')
mycus=db.cursor()
mycus.execute(('create database if not exists vaccin_db'))
kent='\t'*4
cent='\t'*5
pent='\t'*6
def connection3():
    print('Vaccine Connected')

def vaccn_rgtr():
    print()
    print(cent,'------------------------')
    print(cent,'|  Registeration Page  |')
    print(cent,'------------------------')
    print()
    print(cent,'-----------------------------')
    print(cent,'| 1. 1st dose registeration |')
    print(cent,'| 2. 2nd dose registeration |')
    print(cent,'| 3. Certificate            |')
    print(cent,'| 4. Main Menu              |')
    print(cent,'-----------------------------')
    while True:
        uc=input('Enter choice: ')
        if uc=='1':
            print()
            print(cent,'**Enter Beneficiary Details**'.upper())
            print()
            return firstdose()
            
        
        elif uc=='2':
            return seconddose()
            

        elif uc=='3':
            return cert()
        elif uc=='4':
            val=[0]
            return val
        else:
            print('\nInvalid Choice......'.center(100))
def firstdose():
    mycus=db.cursor()
    mycus.execute('create table if not exists details(Name varchar(30),Age int(3),Aadhar_N bigint(12),Phone_N bigint(10),gen varchar(10),\
agp varchar(8),vcc varchar(10),D1 varchar(1),D2 varchar(1),unique(aadhar_n))')
    while True:
        nm=input('Enter name of candidate: ')
        ag=int(input('Enter the age: '))
        #global aadn ###########
        aadn=input('Enter aadhar number: ')
        if len(aadn)!=2: #12
            print(cent,'invalid aadhar number')
            continue
        phn=input('Enter phone number: ')
        if len(phn)!=1: #10
            print(cent,'invalid phone number')
            continue
        else:
            break
    
    while True:
        print('\nGender \n1.Male \n2.Female \n3.Others\n')
        ch=int(input('Enter Your choice: '))
        if ch==1:
            gen='Male'
            break
        elif ch==2:
            gen='Female'
            break
        elif ch==3:
            gen='Others'
            break
        else:
            print('Select correct option')
            continue

        
    print('\nAge Group:')
    age_group={1:'12-14',2:'15-18',3:'18+'}
    for i in age_group:
        print(i,':',age_group[i])
    print()
    ch=int(input('Enter Your Choice: '))
    agp=age_group[ch]
    print('\nVaccine:')
    vaccine={1:'Covishield',2:'Covaxin',\
             3:'Sputnik V',4:'ZyCoV-D',5:'Corbevax'}
    for i in vaccine:
        print(i,':',vaccine[i])
    print()
    ch=int(input('Enter Your Choice: '))
    vcc=vaccine[ch]
    val=((nm,ag,aadn,phn,gen,agp,vcc,'Y','N'))
    mycus=db.cursor()
    return val


def seconddose():
    mycus=db.cursor()
    mycus.execute('create table if not exists details(Name varchar(30),Age int(3),Aadhar_N bigint(12),Phone_N bigint(10),gen varchar(10),\
agp varchar(8),vcc varchar(10),D1 varchar(1),D2 varchar(1))')
    while True:
        mycus=db.cursor()
        aadn=input('Enter aadhar number: ')
        if len(aadn)!=2: #12
            print(cent,'invalid aadhar number')
            continue
        mycus.execute('select D1,D2 from details where aadhar_n='+str(aadn))
        for i in mycus:
            if i[0]=='Y':
                if i[1]=='N':
                    print()
                    print(cent,'**Registration Found**')
                    print()
                    return aadn
                print(cent,'**Already Fully Vaccinated**')    
                    
                
            elif i[0]=='N':
                print()
                print(cent,'**Register for 1st Dose first**')
                vaccn_rgtr()
                
def cert():
    mycus=db.cursor()
    mycus.execute('create table if not exists details(Name varchar(30),Age int(3),Aadhar_N bigint(12),Phone_N bigint(10),gen varchar(10),\
agp varchar(8),vcc varchar(10),D1 varchar(1),D2 varchar(1))')
    while True:
        mycus=db.cursor()
        aadn=input('Enter aadhar number: ')
        if len(aadn)!=2: #12
            print(cent,'invalid aadhar number')
            continue
        mycus=db.cursor()
        mycus.execute('select D1 from details where aadhar_n='+str(aadn))
        for i in mycus:
            if i[0]=='Y':
                val=list(i[0])
                return int(aadn)
