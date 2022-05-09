import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='mkpbatch')
    
def addEmp(t):
    db=getConnection()
    sql='insert into emp values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()




def selectAllEmp():
    db=getConnection()
    sql='select * from emp'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def login():
    db=getConnection()
    sql='select name , passw from emp'
    cr=db.cursor()
    cr.execute(sql)
    elist1=cr.fetchall()
    db.commit()
    db.close()
    return elist1


    
def deleteEmp(id):
    db=getConnection()
    sql='delete from  emp where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from emp where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def selectEmpByname(name):
    db=getConnection()
    sql='select * from emp where name=%s'
    cr=db.cursor()
    cr.execute(sql,name)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist3

def updateEmp(t):
    db=getConnection()
    sql='update emp set name=%s,contact=%s,email=%s,passw=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
