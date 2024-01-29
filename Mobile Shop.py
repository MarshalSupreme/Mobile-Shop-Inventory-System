import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="1234",database="mobile_shop")

def user():
    u=input("Enter your name : ")
    admins=["Farish","Shehzad","Joshua"]
    if u in admins:
        a=admin(u)
    else:
        a=customer(u)
    print()
    menu(a)
    
def admin(i):
    print("-------------------- Admins Only --------------------")
    p=input("Enter your password: ")
    if p == '1234':
        print("Welcome ",i)
        return 'admin'
    else:
        print("password incorrect")
        print("returning to main section...","\n") 
        user()
        
def customer(i):
    print("Welcome to our Mobile Shop,",i)
    return 'customer'

def intError(o):
    if o.isdigit():
        o=int(o)
    else:
        print("Input Error: Enter int object !")
        print()
        manipulate()
    return o

def Int_Error(o):
    if o.isdigit():
        o=int(o)
    else:
        print("Input Error: Enter int object !")
        print()
        #menu("user")
    return o

def manipulate():
    while True:
        print()
        print("1: To enter new details.")
        print("2: To update existing details.")
        print("3: To delete existing details.")
        print("4: To go back.")
        print("5: To exit.")
        ch2=input("Enter your choice : ")
        ch2=intError(ch2)
        if ch2 == 1:
            print("1: To enter new details in mobile_details table.")
            print("2: To enter new details in mobile_specifications table.")
            ch3=input("Enter your choice : ")
            ch3=intError(ch3)
            if ch3 == 1:
                print('Enter the following details:-')
                sno=input('Enter Serial No. (in integer) : ')
                sno=intError(sno)
                t=duplicate_key(sno)
                if t==False:
                     continue
                company=input('Enter the company name : ')
                model=input('Enter the model name : ')
                year=input('Enter the year (in integer): ')
                intError(year)              
                cost=input('Enter the cost (in integer): ')
                intError(cost)
                c1=db.cursor()
                insert="insert into mobile_details values(%s,%s,%s,%s,%s);"
                val=(sno,company,model,year,cost)
                c1.execute(insert,val)
                db.commit()
                print('New mobile details added!')
                print()

            elif ch3 == 2:
                print('Enter the following details:-')
                sno=input('Enter Serial No(in integer) : ')
                sno=intError(sno)
                t=unique(sno)
                if t==False:
                     continue
                screen=input('Enter screen inch : ')
                frontcam=input("Enter front camera's pixel(in MP) : ")
                backcam=input("Enter back camera's pixel(in MP) : ")
                display=input('Enter display type : ')
                ram=input('Enter RAM (in GB) : ')
                rom=input('Enter Storage / ROM (in GB): ')
                battery=input('Enter battery capacity : ')
                processor=input('Enter processor : ')
                software=input('Enter software : ')

                c1=db.cursor()
                insert="insert into mobile_specifications values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                val=(sno,screen,frontcam,backcam,display,ram,rom,battery,processor,software)
                c1.execute(insert,val)
                db.commit()
                print('New mobile specifications added!')
            else:
                print("Enter a valid input")
                
        elif ch2 == 2:
            print("1: To update existing details in mobile_details table.")
            print("2: To update existing details in mobile_specifications table.")
            ch3=input("Enter your choice : ")
            ch3=intError(ch3)
            if ch3 == 1:
                sno=input("Enter the serial no. of the mobile whose details you want to change : ")
                print("Enter what you want to update")
                print("""
                        1:sno,
                        2:company,
                        3:model,
                        4:year,
                        5:cost,""")
                n=input("Enter your choice: ")
                n=intError(n)
                l=["SNo","Company","Model","Year","Cost"]
                u=l[n-1]
                newval=input("Enter the new value : ")
                if n==1:
                    t=duplicate_key(newval)
                    if t==False:
                        continue
                c1=db.cursor()
                c1.execute("update mobile_details set "+u+" = \""+newval+"\" where sno = "+sno+";")
                db.commit()
                print('New mobile details updated!')

            elif ch3==2:
                sno=input("Enter the serial no. of the mobile whose specifications you want to change : ")
                print("Enter what you want to update")
                print("""
                        1:sno,
                        2:screen,
                        3:frontcam,
                        4:backcam,
                        5:display,
                        6:ram,
                        7:rom,
                        8:battery,
                        9:processor,
                        10:software""")
                n=input("Enter your choice: ")
                n=intError(n)
                if n==1:
                    t=unique(sno)
                    if t==False:
                        continue
                l=["sno","screen","frontcam","backcam","display","ram","rom","battery","processor","software"]
                u=l[n-1]
                newval=input("Enter the new value : ")
                c1=db.cursor()
                c1.execute("update mobile_specifications set "+u+" = \""+newval+"\" where sno = "+sno+";")
                db.commit()
                print('New mobile specifications updated!')

            else:
                print("Enter a valid input!")
                
        elif ch2 == 3:
            print("1: To delete existing details in mobile_details table.")
            print("2: To delete existing details in mobile_specifications table.")
            ch3=input("Enter your choice : ")
            ch3=intError(ch3)
            if ch3 == 1:
                sno=input("Enter the serial no. of the mobile whose details you want to delete : ")
                sno=intError(sno)
                c1=db.cursor()
                c1.execute("delete from mobile_details where sno = "+str(sno)+";")
                db.commit()
                print("Sucessfully deleted the row")
            elif ch3 == 2:
                sno=input("Enter the serial no. of the mobile whose details you want to delete : ")
                sno=intError(sno)
                c1=db.cursor()
                c1.execute("delete from mobile_specifications where sno = "+str(sno)+";")
                db.commit()
                print("Sucessfully deleted the row")
            else:
                print("Enter a valid input!")
        elif ch2 == 4:
            menu()
            break
        elif ch2 == 5:
            print("-----------------------x-----------------------")
            break
        else:
            print("Enter a valid choice !!!")

def duplicate_key(sno):
    c1=db.cursor()
    c1.execute('select * from mobile_details;')
    data=c1.fetchall()
    l1=[]
    for row in data:
        l1.append(row[0])
    if  sno in l1:
        print("Serial No. already present")
        #manipulate()
        return False
        
        
def unique(sno):
    c1=db.cursor()
    c1.execute('select * from mobile_specifications;')
    data=c1.fetchall()
    l1=[]
    for row in data:
        l1.append(row[0])
    if  sno in l1:
        print("Serial No. already present")
        #manipulate()
        return False
    
def compare():
    print("Enter two mobile's S.no.s to compare theirs specifications : ")
    n=input("Enter first mobile's S.no. :")
    m=input("Enter second mobile's S.no. :")
    n=Int_Error(n)
    m=Int_Error(m)
    c1=db.cursor()
    c1.execute('select * from mobile_details;')
    data=c1.fetchall()
    l1=[]
    l2=[]
    for row in data:
        if row[0]==n:
            if row not in l1:
                l1.append(row)
        elif row[0]==m:
            if row not in l2:
                l2.append(row)
    u='user'
    if l1 == []:
        print("First mobile is not present in table !")
        #menu(u)
    elif l2 == []:
        print("Second mobile is not present in table !")
        #menu(u)
    else:
        for r in l1:
            for det in r:
                if det==r[0]:
                    pass
                elif det==r[-1]:
                    print('',end='')
                elif det==r[3]:
                    print("(",det,")",sep='',end='')
                else:
                    print(det,end=' ')
                c=det
                         
        for r in l2:
            for det in r:
                if det==r[0]:
                    print('',end='\t'*6)
                elif det==r[-1]:
                    print()
                elif det==r[3]:
                    print("(",det,")",sep='',end='')
                else:
                    print(det,end=' ')
                b=det
                
        t=[]
        if c>b:
            e='>'
        elif c<b:
            e='<'
        elif c==b:
            e='='
                    
        ce='='    
        if e=='>':
            ce='<'
        elif e=='<':
            ce='>'
        t.append(ce)
        print('-'*100)    
        print('Cost       :',c,'Rs','\t'*3,'  ',e+'\t'*3+'Cost       :',b,'Rs')
                    
                    
        c1.execute('select * from mobile_specifications;')
        data=c1.fetchall()
        l3=[]
        l4=[]
        s=['S.No.','Screen','FrontCam','BackCam','Display','RAM','Storage','Battery','Processor','Software']
        for row in data:
            if row[0]==n:
                if row not in l3:
                    l3.append(row)
            elif row[0]==m:
                if row not in l4:
                    l4.append(row)
        l=len(l4)
        n=0
        for specs in l3:
            for i in specs:
                if n in [0,4,8,9]:
                    eq=' '
                elif n in [2,3,5,6]:
                    if eval(l3[l-1][n][:-2])>eval(l4[l-1][n][:-2]):
                        eq='>'
                    elif eval(l3[l-1][n][:-2])<eval(l4[l-1][n][:-2]):
                        eq='<'
                    elif eval(l3[l-1][n][:-2])==eval(l4[l-1][n][:-2]):
                        eq='='
                elif n in [7]:
                    if eval(l3[l-1][n][:-3])>eval(l4[l-1][n][:-3]):
                        eq='>'
                    elif eval(l3[l-1][n][:-3])<eval(l4[l-1][n][:-3]):
                        eq='<'
                    elif eval(l3[l-1][n][:-3])==eval(l4[l-1][n][:-3]):
                        eq='='
                else:
                    if l3[l-1][n]>l4[l-1][n]:
                        eq='>'
                    elif l3[l-1][n]<l4[l-1][n]:
                        eq='<'
                    elif l3[l-1][n]==l4[l-1][n]:
                        eq='='
                t.append(eq)
                print ("{:<10} {:<1} {:<30} {:<19} {:<10} {:<1} {:<20}".format(s[n],":",specs[n],eq,s[n],":",l4[l-1][n]))
                n+=1
            less=t.count('<')
            great=t.count('>')
            if less > great:
                print("second one is better than first")
            elif less < great:
                print("first one is better than second")
            elif less == great:
                print("Both are similar")

def print_details(data):
    l1=[]
    for row in data:
        if row not in l1:
            l1.append(row)
    for r in l1:
        for det in r:
            if det==r[-1]:
                cost='Cost:'+str(det)+' Rs'
            else:
                sno='S.No. '+str(r[0])
                name='\t'+r[1]+' '+r[2]+' '+'('+str(r[3])+')'
        print("{:<5} {:<30} {:<10} ".format(sno,name,cost))

def menu(a="admin"):
    print("MENU:-","\n")
    print("Enter:")
    while True:
        print()
        if a == 'admin':
            print("0: To enter new details or, update or delete existing details. ")
        print("1: To enter a mobile's S.no. and get its details and specifications. ")
        print("2: To display the names of mobile companies which are available here. ")
        print("3: To display all the mobile phones released in a year of your choice. ")
        print("4: To display all the mobile phones within a price range. ")
        print("5: To display all the mobile phones belonging to a company of your choice. ")
        print("6: To compare specifications of two mobile phones ,if S.No.s of both given. ")
        print("7: To sort mobiles according to cost or name. ")
        print("8: To show all mobile details present in the table")
        print("9: To EXIT")
        ch=input("Enter your choice : ")
        if a == 'admin':
            if ch.isdigit():
                if int(ch)==0:
                    manipulate()
                    break
            else:
                print("Enter int value for choice !")
        ch=Int_Error(ch)
        if ch==1:
            n=input("Enter a mobile's S.no. to get its details and specifications : ")
            n=Int_Error(n)
            c1=db.cursor()
            c1.execute('select * from mobile_details;')
            data=c1.fetchall()
            l1=[]
            for row in data:
                if row[0]==n:
                    if row not in l1:
                        l1.append(row)
            if l1 == []:
                print("Serial no. not there in the table !")
            for r in l1:
                for det in r:
                    if det==r[0]:
                        print("",end='\t'*2)
                    elif det==r[-1]:
                        print('\t','Cost:',det,'Rs')
                    elif det==r[3]:
                        print("(",det,")",sep='',end='')
                    else:
                        print(det,end=' ')
                print()
                
            c1.execute('select * from mobile_specifications;')
            data=c1.fetchall()
            l2=[]
            s=['S.No.','Screen','FrontCam','BackCam','Display','RAM','Storage','Battery','Processor','Software']
            for row in data:
                if row[0]==n:
                    if row not in l2:
                        l2.append(row)
            for r in l2:
                n=0
                for specs in r:
                    print(s[n],":",specs)
                    n+=1
        
        
        elif ch==2:
            c1=db.cursor()
            c1.execute('select distinct Company from mobile_details;')
            data=c1.fetchall()
            count=c1.rowcount
            print('Total number of Mobile companies available here = ',count)
            print('And they are :-')
            for row in data:
                print(row[0])
            print()
            
        
        elif ch==3:
            c1=db.cursor()
            c1.execute('select * from mobile_details;')
            data=c1.fetchall()
            y=input("Enter a year to display all mobiles released in that year : ")
            y=Int_Error(y)
            l1=[]
            for row in data:
                if row[3]==y:
                    if row not in l1:
                        l1.append(row)
            count=len(l1)
            print('Total number of Mobile phones available here, released in ',y,' = ',count)
            if count != 0:
                print('And they are :-')
            for r in l1:
                for det in r:
                    if det==r[0]:
                        print("S.No.",det,end='\t'*2)
                    elif det==r[3]:
                        print("(",det,")",sep='',end='')
                    elif det==r[-1]:
                        print('\t','Cost:',det,'Rs')
                    else:
                        print(det,end=' ')
                print()
            
        
        elif ch==4:
            c1=db.cursor()
            c1.execute('select * from mobile_details;')
            data=c1.fetchall()
            print("To display all the mobile phones within a price range")
            p1=input("Enter from which price the range should start : ")
            p2=input("Enter price upto which the range should end : ")
            p1=Int_Error(p1)
            p2=Int_Error(p2)
            if not p1<=p2:
                print("Range Error: From price should be greater or equal than to the upto price !")
                menu()
            l1=[]
            for row in data:
                if row[-1] in range(p1,p2+1):
                    if row not in l1:
                        l1.append(row)
            count=len(l1)
            print('Total number of Mobile phones available here, beteen price range ',p1,'and',p2,' = ',count)
            if count != 0:
                print('And they are :-')
            for r in l1:
                for det in r:
                    if det==r[0]:
                        print("S.No.",det,end='\t'*2)
                    elif det==r[3]:
                        print("(",det,")",sep='',end='')
                    elif det==r[-1]:
                        print('\t','Cost:',det,'Rs')
                    else:
                        print(det,end=' ')
                print()
                
        
        elif ch==5:
            c1=db.cursor()
            c1.execute('select * from mobile_details;')
            data=c1.fetchall()
            print("To display all the mobile phones from a particular company")
            cn=input("Enter company name : ")
            l1=[]
            for row in data:
                if row[1].lower() == cn.lower():
                    if row not in l1:
                        l1.append(row)
            count=len(l1)
            print('Total number of Mobile phones available here, from ',cn,'=',count)
            if count != 0:
                print('And they are :-')
            for r in l1:
                for det in r:
                    if det==r[0]:
                        print("S.No.",det,end='\t'*2)
                    elif det==r[3]:
                        print("(",det,")",sep='',end='')
                    elif det==r[-1]:
                        print('\t','Cost:',det,'Rs',end='\t')
                    else:
                        print(det,end=' ')
                print()
            
        
        elif ch==6:
            compare()    
        
        
        elif ch==7:
            print("Choose one of the option to sort mobiles according to it: ")
            print("1: To sort according to name in ascending order.")
            print("2: To sort according to name in descending order.")
            print("3: To sort according to cost in ascending order.")
            print("4: To sort according to cost in descending order.")
            sort=input("Enter choice : ")
            sort=Int_Error(sort)
            if sort==1:
                c1=db.cursor()
                c1.execute('select * from mobile_details order by company,model;')
                data=c1.fetchall()
                
            elif sort==2:
                c1=db.cursor()
                c1.execute('select * from mobile_details order by company desc,model desc;')
                data=c1.fetchall()
                
            elif sort==3:
                c1=db.cursor()
                c1.execute('select * from mobile_details order by Cost;')
                data=c1.fetchall()
                
                 
            elif sort==4:
                c1=db.cursor()
                c1.execute('select * from mobile_details order by Cost desc;')
                data=c1.fetchall()
        
            else:
                print("Enter a valid choice!")
                menu()
            print("The sorted data:")
            print_details(data)
            print()
            
        elif ch == 8 :
            c1=db.cursor()
            c1.execute('select * from mobile_details;')
            data=c1.fetchall()
            print("All the mobiles present in our shop are :- ")
            print_details(data)
            print()
            
        elif ch == 9 :
            print("Thank You!")
            print("Visit again....")
            print("Have a nice day :)")
            break
        
        else:
            print("Enter a valid choice ... ")
            print()
            
user()