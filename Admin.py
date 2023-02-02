import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='root')
mycus=db.cursor()
mycus.execute('create database if not exists vaccin_db')
import random
import vacc
db=mysql.connector.connect(host='localhost',user='root',passwd='root',database='vaccin_db')

cent='\t'*5
pent='\t'*6

def connection1():
    print('Admin Connected')

'''    
def login():
    user=input("Enter Admin's User_Name: ")
    passw=input('Enter Password: ')
    mycus=db.cursor()
    mycus.execute('select * from login_info')
    if (user,passw) in mycus:
        print('Logged in')
    show_all()

def show_all():
    mycus=db.cursor()
    mycus.execute('select distinct * from details')
    for i in mycus:
        print(i)
'''    
            
  
def location():
    print(cent,'-----------------------------')
    print(cent,'| Select Vaccination Center |')
    print(cent,'-----------------------------')
    mycus=db.cursor()
    mycus.execute('create table if not exists location(\
S_No int auto_increment primary key,\
hospital varchar(50),address char(30),district char(20)\
,state char(20),pin_code char(10))')
    sql_c="INSERT INTO LOCATION values"
        
    val=(('Sahar CHC' ,'Sahar', 'Auraiya', 'Uttar Pradesh', '206248'),\
            ('Achalda CHC', 'Achalda', 'Auraiya', 'Uttar Pradesh', '206241'),\
            ('Airwakatra CHC','Airawakatra' , 'Auraiya',' Uttar Pradesh',
             '206252'),\
            ('Ajeetmal CHC' ,'Ajeetmal', 'Auraiya', 'Uttar Pradesh', '206121'),\
            ('Bidhuna CHC ','Bidhuna', 'Auraiya', 'Uttar Pradesh', '206243'),\
            ('Dibiyapur CHC','DIBIYAPUR', 'Auraiya', 'Uttar Pradesh', '206244'),\
            ('50Beds District Hospital 2nd', 'Tilak Nagar Auraiya',
             'Auraiya', 'Uttar Pradesh', '206122'),\
            ('50BED HOSPITAL AURAIYA' ,'TILAK NAGAR AURAIYA' ,
             'Auraiya', 'Uttar Pradesh', '206122'))
    
    for i in range(len(val)):
        mycus=db.cursor()
        try:
            mycus.execute(sql_c+str(((i+1,)+val[i])))
        except:
            break
    db.commit()
    mycus=db.cursor()
    mycus.execute('select * from location')
    print('\t'*4,'-'*43)
    for j in mycus:
        
        print('\t'*4,'| ',j[0],' | ',j[2],' '*(20-len(j[2])),'| ',j[5],' |')
    print('\t'*4,'-'*43)    
    while True:
        mycus=db.cursor()
        iut=int(input('Enter your area pincode: '))
        mycus.execute('select * from location')
        for i in mycus:
            if str(iut) in i:
                hloc=i[1]
                print()
                print('\t'*4,'Your vaccination center is at',hloc)
                print()   
                return hloc
        else:
            print(cent,'!!incorrect pincode!!'.upper)
            continue
        break


def certificate(val):
    
    db=mysql.connector.connect(host='localhost',user='root',passwd='root',database='vaccin_db')
    mycus=db.cursor()
    cent='\t'*3
    mycus=db.cursor()
    mycus.execute('select distinct * from details where aadhar_n='+str(val))
    for i in mycus:
        information=i
        break
   
    mycus=db.cursor()
    mycus.execute('select distinct * from addr where aadhar_n='+str(val))
    for i in mycus:
        info=i
        break
    nm=['Neha','Suman','Shanti','Ram','Aman']
    
    from datetime import date
    import string
    rs=str(''.join(random.choices(string.ascii_uppercase + string.digits, k=9)))
    
    
    if information[7]=='Y':
        if information[8]=='Y':
            st='Fully Vaccinated(2 Dose)'
            nd='2/2'
        if information[8]!='Y':
            st='Partially Vaccinated(1 Dose)'
            nd='1/2'
            
    data=[
        'Beneficiary Details:-' ,
        ' ',
        'Beneficiary Name:',
        'Age:',
        'Gender:',
        'ID verified:',
        'Beneficiary Reference Id:',
        'Vaccination Status:',
        ' ',
        'Vaccination Details: ',
        ' ',
        'Vaccine Name:',
        'Vaccine Type:',
        'Manufacturer:',
        'Dose Number:',
        'Date of Dose:',
        'Batch Number:',
        'Vaccinated By:',
        'Vaccinated At:',
     ]
    value=[
        ' ',
        ' ',
        information[0],
        information[1],
        information[4],
        information[2],
        random.randint(10**13,9**14),
        st,
        ' ',
        ' ',
        ' ',
        information[6],
        'COVID-19 vaccine,inactivated virus',
        'Bharat Biotech,India',
        nd,
        date.today(),
        rs,
        random.choice(nm),
        info[1],
        ]
    sz=len(value)
    print(' '*4,'-'*(26+36+9))
    for i in range (sz):
        
        print(' '*4,'|',data[i],' '*(26-len(data[i])),'|',value[i],' '*(36-len(str(value[i]))),'|')
    print(' '*4,'-'*(26+36+9))
        
 
def otp():
    print(pent,'-------------')
    print(pent,'|    OTP    |')
    print(pent,'-------------')
    while True:
        o=random.randrange(1000,10000)
        print(o)
        print()
        inpt=int(input('Enter OTP: '))
        
        if o==inpt:
            print()
            return
        else:
            print(cent,'***Incorrect OTP***')
            print()
         
def captcha():
    print(pent,'-------------')
    print(pent,'|  Captcha  |')
    print(pent,'-------------')
    while True:
        a=random.randrange(20)
        b=random.randrange(20)
        c=a+b
        st=str(str(a)+' + '+str(b)+' = ')
        inp=int(input(st))
        if c==inp:
            print(cent,'*** Sucessfully Logged In ***')
            return
        else:
            print(cent,'!!! Re-enter captcha !!!\n')   

    

