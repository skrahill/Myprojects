import pymysql as p

def getconnect():
    return p.connect(host="localhost",user="root",password="",database="itvdb")


def readdata():
    db=getconnect()
    cr=db.cursor()

    sql="select * from itvtable"
    cr.execute(sql)

    data=cr.fetchall()

    for d in data:
        print(f"{d[0]:^3} {d[1]:^10} {d[2]:^20} {d[3]:^15}")

    db.commit()
    db.close()

def insertdata():
    i_d=input("enter employee Id: ").strip()
    name=input("enter employee Name: ").strip()
    
    email=input("enter employee Email: ").strip()
    place=input("enter employee place: ").strip()
  

    t=(i_d,name,email,place)

    db=getconnect()
    cr=db.cursor()

    sql="insert into itvtable values(%s,%s,%s,%s);"
    cr.execute(sql, t)

    print("data inserted\n")
    db.commit()
    db.close()


def deletedata():
    i_d=input("enter employee id here to delete:").strip()
    db=getconnect()
    cr=db.cursor()

    sql="delete from itvtable where id=%s;"
    
    cr.execute(sql, i_d)
    print("employee details deleted successfully")
    db.commit()
    db.close()

def showdata():
    i_d=input("enter employee id :").strip()
    db=getconnect()
    cr=db.cursor()

    sql="select * from itvtable where id=%s;"
    cr.execute(sql, i_d)

    data=cr.fetchall()

    db.commit()
    db.close()
    


    for i in data:
        print(f"{i[0]:^3} {i[1]:^10} {i[2]:^20} {i[3]:^15}\n")

def updatedata(uemp):
    db=getconnect()
    cr=db.cursor()

    if uemp == "1":
        i_d = input("Enter Employee Id : ").strip()
        name = input("Enter New Name : ").strip()
        t = (name, i_d)
        sql = "update itvtable set name=%s where id = %s;"
        cr.execute(sql,t)
        print("Data updated")

    elif uemp == "2":
        i_d = input("Enter Employee Id : ").strip()
        email = input("Enter New Email : ").strip()
        t = (email, i_d)
        sql = "update itvtable set email=%s where id = %s;"
        cr.execute(sql,t)
        print("Data updated")

    elif uemp == "3":
        i_d = input("Enter Employee Id : ").strip()
        place = input("Enter place : ").strip()
        t = (place, i_d)
        sql = "update itvtable set palce=%s where id = %s;"
        cr.execute(sql,t)
        print("Data updated")


    elif uemp == "4":
        i_d = input("Enter Employee Id : ").strip()
        nid = input("Enter New Employee Id : ").strip()
        t = (nid, i_d)
        sql = "update itvtable set id=%s where id = %s;"
        cr.execute(sql,t)
        print("Data updated")


   
        
    elif uemp=="5":
        uemploop()

    db.commit()
    db.close()



def uemploop():

    while True:
        
        print("\nEnter 1 to Show Emp Full Record")
        print("Enter 2 to Add Employee")
        print("Enter 3 to Update Employee Details")
        print("Enter 4 to Delete Employee Record")
        print("Enter 5 to show Employee Data")
        print("Enter 6 to Exit\n")

        choice = input("Enter your Choice : ").lstrip()
        print("\n")

        if choice == "1":
            readdata()

        elif choice == "2":
            insertdata()

        elif choice == "3":

            print("\nEnter 1 to Update Employee Name")
            print("Enter 2 to Update Employee Email")
            print("Enter 3 to Update Employee place")
           
            print("Enter 4 to Update Employee ID")
            print("Enter 5 to Exit\n")

            uemp=input("Enter Your Choice:").strip()
            updatedata(uemp)

        elif choice == "4":
            deletedata()

        elif choice == "5":
            showdata()

        elif choice == "6":
            print("exit")
            break
        else:
            print("Entered choice is invalid!!please choose again.\n")
uemploop()




    
        


    
    

    
    









    

    
