import pymysql
import pymysql
import getpass

user = "root"
password = getpass.getpass("Enter your MySQL password: ")

db = pymysql.connect(
    host='localhost',
    user=user,
    passwd=password
)

cur=db.cursor()
cur.execute("show databases")
w=cur.fetchall()
flights=['IG5882','SJ6781','AI9218','VI7219','IG4863']
if ('airlines_management_system',) in w:
    cur.execute("use Airlines_Management_System;")
    cur.execute("ALTER TABLE user_data MODIFY mobile BIGINT;")
    cur.execute("ALTER TABLE ticket_record MODIFY mobile BIGINT;")
    pass
else:
    cur.execute("create database Airlines_Management_System;")
    cur.execute("use Airlines_Management_System;")
    cur.execute("create table flights(flight_code varchar(6),airlines_name varchar(20),departure varchar(10),arrival varchar(10),date date,time time,duration time,gate int(2),status varchar(10),price int(5),pilot char(7));")
    cur.execute("insert into flights value ('IG5882','IndiGo','Bangalore','Chennai','2024-05-13','19:00','1:00',16,'On Time',12500,'APJ2584');")
    db.commit()
    cur.execute("insert into flights value ('SJ6781','SpiceJet','Hyderabad','Lucknow','2024-05-13','14:00','2:15',07,'On Time',19285,'TYC7293');")
    cur.execute("insert into flights value ('AI9218','AirIndia','Goa','Indore','2024-05-13','17:45','1:37',11,'Delayed',18250,'TRW6720');")
    cur.execute("insert into flights value ('VI7219','Vistara','Delhi','Mumbai','2024-05-13','20:00','1:25',25,'Delayed',24500,'JKL486');")
    cur.execute("insert into flights value ('IG4863','IndiGo','Delhi','Jammu','2024-05-13','5:00','2:18',18,'On Time',26540,'VCG580');")
    cur.execute("create table user_data(name varchar(20),mobile int(10),password varchar(20));")
    cur.execute("create table emp_data(name varchar(20),emp_id char(7),password varchar(20), designation varchar(10));")
    cur.execute("create table ticket_record(ticket char(7),mobile int(10),flight_code varchar(6));")
    cur.execute("create table duty(emp_id char(7),flight_code varchar(6));")
    cur.execute("insert into emp_data value ('Sumit','YUJ889','22ad40','Checker');")
    db.commit()
    cur.execute("insert into emp_data value ('Reena','JKL486','18yu67','Pilot');")
    db.commit()
    cur.execute("insert into emp_data value ('Anjali','RRD219','15ih94','AirHostess');")
    db.commit()
    cur.execute("insert into duty value ('YUJ889','AI9218');")
    db.commit()
    cur.execute("insert into duty value ('JKL486','VI7219');")
    db.commit()
    cur.execute("insert into duty value ('RRD219','IG4863');")
    db.commit()
    for i in flights:
        cur.execute("create table %s (seat int(3),passenger varchar(20),ticket char(7));"%i)
        db.commit()
    for i in flights:
        for j in range (1,51):
            cur.execute("insert into %s value ('%d',NULL,NULL);"%(i,j))
            db.commit()
    for i in range (1,51):
        o="AWB"+str(1200+i)
        cur.execute("insert into ticket_record value ('%s',NULL,NULL);"%o)
        db.commit()

    
    print("Database created successfully!!")

def schedule():
    cur.execute("select * from flights;")
    w=cur.fetchall()
    for i in range(len(w)):
        print("S.NO.:",i)
        print("Flight Code:",w[i][0])
        print("Airlines Name:",w[i][1])
        print("Departure:",w[i][2])
        print("Arrival:",w[i][3])
        print("Date:",w[i][4])
        print("Time:",w[i][5])
        print("Duration:",w[i][6])
        print("Gate:",w[i][7])
        print("Status:",w[i][8])
        print("\n\n")

def login1():
    ph=int(input("Enter Mobile Number:"))
    cur.execute("select mobile from user_data;")
    w=cur.fetchall()
    mobile_numbers = [mobile[0] for mobile in w]
    if ph in mobile_numbers:
        p=input("Enter Password:")
        cur.execute("select password from user_data where mobile = %d;"%ph)
        u=cur.fetchone()
        if(p==u[0]):
            print("Login Successfully!!")
            return ph
        else:
            print("Password is incorrect!")
            return -1
    else:
        print("Mobile Number is not registered!\nPlease Create New Account")
        return -1

def signup():
    ph=int(input("Enter Mobile Number:"))
    cur.execute("select mobile from user_data;")
    w=cur.fetchall()
    if(ph in w):
        print("Mobile Number is already registered!\nPlease Login that Account")
        return -1
    else:
        n=input("Enter Name:")
        p=input("Enter Password:")
        cur.execute("insert into user_data value('%s',%d,'%s');"%(n,ph,p))
        db.commit()
        print("Sign Up Successfully!!")
        return ph
    
def login2():
    emp=input("Enter Employee ID:")
    cur.execute("select emp_id from emp_data;")
    w=cur.fetchall()
    e = [str(ID[0]) for ID in w]
    if emp in e:
        p=input("Enter Password:")
        cur.execute("select password from emp_data where emp_id = '%s';"%emp)
        u=cur.fetchone()
        if(p==u[0]):
            print("Login Successfully!!")
            return emp
        else:
            print("Password is incorrect!")
            return -1
    else:
        print("NO employee is registered with this employee ID!\nPlease contact Admin")
        return -1

    
print('AIRLINES MANAGEMENT SYSTEM')
while True:
    print('1.View Flight Schedule')
    print('2.Passanger')
    print('3.Employee')
    print('4.Admin')
    choice=int(input('Enter the choice:'))
    if choice==1:
        schedule()
    elif choice==2:
        print("Login/Sign Up with your mobile number:")
        print('1.Login')
        print('2.Sign Up')
        choose=int(input('Enter the choice:'))
        if choose==1:
            ph=login1()
            if ph==-1:
                continue
        elif choose==2:
            ph=signup()
            if ph==-1:
                continue
        print("1. View Flight Schedule\n2. Book New Ticket\n3. View Booked Tickets\n4. Update your Ticket\n5. Cancel Ticket")
        a=int(input('Enter the choice:'))

        if a==1:
            schedule()

        elif a==2:
            dep=input("From: ")
            arr=input("To: ")
            date=input("Date: ")
            nop=int(input("Number of Passengers: "))
            cur.execute("select * from flights where departure = '%s' and arrival = '%s' and date = '%s';"%(dep,arr,date))
            w=cur.fetchall()
            print("Available Flights:\n")
            for i in range(len(w)):
                print("S.NO.:",i)
                print("Flight Code:",w[i][0])
                print("Airlines Name:",w[i][1])
                print("Departure:",w[i][2])
                print("Arrival:",w[i][3])
                print("Date:",w[i][4])
                print("Time:",w[i][5])
                print("Duration:",w[i][6])
                print("Price:",w[i][9])
                print("\n\n")
            b=int(input("Select S.No. of flight you want to book:"))
            print("Available Seats:\n")
            f=w[b][0]
            cur.execute("select seat from %s where ticket is NULL;"%f)
            w=cur.fetchall()
            if w:
                for seat in w:
                    print(seat[0])
            else:
                print("No available seats found for this flight.")
            print("\n")
            for i in range(nop):
                s=int(input("Enter Seat Number for Passenger "+str(i)+":"))
                n=input("Enter Name of Passenger "+str(i)+":")
                cur.execute("select ticket from ticket_record where mobile is NULL;")
                u=cur.fetchone()
                t=u[0]
                cur.execute("update %s set passenger='%s', ticket='%s' where seat=%d;"%(f,n,t,s))
                cur.execute("update ticket_record set mobile=%d, flight_code='%s' where ticket='%s';"%(ph,f,t))
                db.commit()
            print("Ticket Booked Successfully!!")

        elif a==3:
            print("Your Booked Tickets:\n")
            cur.execute("select ticket,flight_code from ticket_record where mobile=%d;"%ph)
            w=cur.fetchall()
            for i in range(len(w)):
                cur.execute("select * from flights where flight_code='%s';"%w[i][1])
                z=cur.fetchone()
                cur.execute("select seat, passenger from %s where ticket= '%s';"%(w[i][1],w[i][0]))
                y=cur.fetchone()
                print("Ticket ID:",w[i][0])
                print("Flight Code:",w[i][1])
                print("Passenger Name:",y[1])
                print("Airlines Name:",z[1])
                print("Departure:",z[2])
                print("Arrival:",z[3])
                print("Date:",z[4])
                print("Time:",z[5])
                print("Duration:",z[6])
                print("Gate:",z[7])
                print("Seat:",y[0])
                print("Price:",z[9])
                print("\n\n")

        elif a==4:
            print("Your Booked Tickets:\n")
            cur.execute("select ticket,flight_code from ticket_record where mobile=%d;"%ph)
            w=cur.fetchall()
            for i in range(len(w)):
                print("S.NO.:",i)
                print("Ticket ID:",w[i][0])
            print("\n")
            p=int(input("Select S.No. of ticket you want to update:"))
            cur.execute("select seat,passenger from %s where ticket='%s';"%(w[p][1],w[p][0]))
            u=cur.fetchone()
            print("Your Booked Seat:",u[0])
            cur.execute("select seat from %s where ticket is NULL;"%w[p][1])
            v=cur.fetchall()
            print("Available Seats:\n")
            for i in range(len(v)):
                print(v[i][0])
            print("\n")
            q=int(input("Select New seat number you want:"))
            cur.execute("update %s set passenger='%s', ticket='%s' where seat='%s';"%(w[p][1],u[1],w[p][0],q))
            cur.execute("update %s set passenger='NULL', ticket='NULL' where seat='%s';"%(w[p][1],u[0]))
            db.commit()
            print("Seat Updated Successfully!!")
            
        elif a==5:
            print("Your Booked Tickets:\n")
            cur.execute("select ticket,flight_code from ticket_record where mobile=%d;"%ph)
            w=cur.fetchall()
            for i in range(len(w)):
                print("S.NO.:",i)
                print("Ticket ID:",w[i][0])
            print("\n")
            p=int(input("Select S.No. of ticket you want to cancel:"))
            cur.execute("update %s set passenger='NULL', ticket='NULL' where ticket='%s';"%(w[p][1],w[p][0]))
            cur.execute("update ticket_record set mobile=NULL, flight_code=NULL where ticket='%s';"%w[p][0])
            db.commit()
            print("Ticket Cancelled Successfully!!")

    elif choice==3:
        emp=login2()
        if emp==-1:
            continue
        print("1. View Flight Schedule\n2. View Your Schedule")
        a=int(input('Enter the choice:'))
        if a==1:
            schedule()
        elif a==2:
            cur.execute("select name, designation from emp_data where emp_id= '%s';"%emp)
            u=cur.fetchone()
            print("Name:",u[0])
            print("Designation:",u[1])
            cur.execute("select flight_code from duty where emp_id='%s';"%emp)
            w=cur.fetchall()
            for i in range(len(w)):
                print("S.NO.:",i)
                print("Flight Code:",w[i][0])
                print("\n")
            print("Please Check the Flight Details & report 1 hour before flight scheduled time")

    elif choice==4:
        print("Admin System is highly secured and restricted, only limited people have its access\nIf you are not from Admin Department Please leave this tab!")
        p=input("Enter Password:")
        if p=='12345678':
            "Login Successfully!!"
        else:
            "Wrong Password!"
        print("1. View Flight Schedule\n2. Add Flight\n3. Update Duty\n4. Update Status\n5. Cancel Flight\n6. Add Employee\n7. Remove Employee")  
        a=int(input('Enter the choice:'))
        if a==1:
            schedule()
        elif a==2:
            fc=input("Enter Flight Code:")
            an=input("Enter Name of Airlines:")
            dp=input("Enter Departure:")
            ar=input("Enter Arrival:")
            dt=input("Enter Date:")
            tm=input("Enter Time:")
            dr=input("Enter Duration:")
            gt=input("Enter Gate:")
            st=input("Enter Status:")
            pr=int(input("Enter Price:"))
            pl=input("Enter Pilot:")
            cur.execute("insert into flights value ('%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,'%s');"%(fc,an,dp,ar,dt,tm,dr,gt,st,pr,pl))
            db.commit()
            cur.execute("create table %s (seat int(3),flight_code varchar(6),ticket char(7));"%fc)
            for j in range (1,51):
                cur.execute("insert into %s value (%d,NULL,NULL);"%(fc,j))
                db.commit()
            print("Flight Added Successfully!!")
        elif a==3:
            emp=input("Enter Employee ID of employee you want to change duty:")
            cur.execute("select flight_code from duty where emp_id='%s';"%emp)
            u=cur.fetchone()
            print("Current Duty:",u)
            new_duty=input("Enter New Duty Flight Code:")
            cur.execute("update duty set flight_code='%s' where emp_id='%s';"%(new_duty,emp))
            print("Duty Updated Successfully!!")
        elif a==5:
            fc=input("Enter Flight Code:")
            cur.execute("update flights set status='Cancelled' where flight_code='%s';"%fc)
            cur.execute("drop table %s;"%fc)
            print("Flight Cancelled Successfully!!")
        elif a==4:
            fc=input("Enter Flight Code:")
            cur.execute("select status from flights where flight_code='%s';"%fc)
            u=cur.fetchone()
            print("Current Status:",u[0])
            st=input("Enter New Status:")
            cur.execute("update flights set status='%s' where flight_code='%s';"%(st,fc))
            print("Status Updated Successfully!!")
        elif a==6:
            emp=input("Enter New Employee ID:")
            psw=input("Enter Employee Password:")
            nm=input("Enter Employee Name:")
            dsg=input("Enter Employee Designation:")
            cur.execute("insert into emp_data value ('%s','%s','%s','%s');"%(nm,emp,psw,dsg))
            db.commit()
            print("Employee Added Successfully!!")
        elif a==7:
            emp=input("Enter Employee ID you want to remove:")
            cur.execute("delete from emp_data where emp_id='%s';"%emp)
            db.commit()
            print("Employee Removed Successfully!!")
