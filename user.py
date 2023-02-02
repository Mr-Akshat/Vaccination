import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='root',database='vaccin_db')
mycus=db.cursor()
mycus.execute('create table if not exists login_info(UserN char(20),Paswd varchar(8), unique(usern))')
cent='\t'*5


def connection2():
    print('User Connected')

def signup():
    while True:
        mycus=db.cursor()
        un= input('Enter User_name: ')
        pd=input('Create password: ')
        pd1=input('Confirm password: ')
        val='insert ignore into login_info values'+str((un,pd1))
        
        if pd==pd1:
            mycus.execute(val)
            db.commit()
            print()
            print(cent,'*** Account Created ***'.upper())
            break
        else:
            print()
            print(cent,'!!! Password not Confirmed !!!'.upper())
            print()
        

def login():
    while True:
        mycus=db.cursor()
        un= input('Enter User_name: ')
        pd=input('Enter password: ')
        mycus.execute('select distinct * from login_info')
        for i in mycus:
            if (un,str(pd))==i:
                return
                              
        else:
            print('\n',cent,'!!!Invalid Username or password!!!'.upper())
            bk=input("Enter 1 to Signup OR press ENTER to try again:")
            print()
            if bk=='1':
                signup()



