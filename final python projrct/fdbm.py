import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='itvbank')
def adduser(t):
    db=getConnection()
    sql='insert into account values(%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def bal(AccountNumber):
    db=getConnection()
    sql="select Balance from account where AccountNumber=%s"
    cr=db.cursor()
    cr.execute(sql,(AccountNumber))
    row=cr.fetchone()
    db.commit()
    db.close()
    return row

def deposite(depamt,AccountNumber):
    db=getConnection()
    cr=db.cursor()
    r=bal(AccountNumber)
    tamt=int(r[0])+depamt
    sql="update account set Balance=%s where AccountNumber=%s"
    cr.execute(sql,(tamt,AccountNumber))
    db.commit()
    db.close()


def withdraw(widamt,AccountNumber):
    db=getConnection()
    cr=db.cursor()
    r=bal(AccountNumber)
    tamt=int(r[0])- widamt
    if tamt<0:
        return 0
    sql="update account set Balance=%s where AccountNumber=%s"
    cr.execute(sql,(tamt,AccountNumber))
    db.commit()
    db.close()



def login():
    db=getConnection()
    sql='select AccountNumber , CustomerName  from account'
    cr=db.cursor()
    cr.execute(sql)
    elist1=cr.fetchall()
    db.commit()
    db.close()
    return elist1

def selectall(a):
    db=getConnection()
    sql='select * from account where AccountNumber=%s'
    cr=db.cursor()
    cr.execute(sql,a)
    elist=cr.fetchone()
    db.commit()
    db.close()
    return elist

def selectbyaccno(t):
    db=getConnection()
    sql='select * from account where AccountNumber =%s'
    cr=db.cursor()
    cr.execute(sql,t)
    elist2=cr.fetchall()
    db.commit()
    db.close()
    return elist2[0]

def deleteEmp(acc):
    db=getConnection()
    sql='delete from  account where AccountNumber=%s'
    cr=db.cursor()
    cr.execute(sql,acc)
    db.commit()
    db.close()

def update(t):
    db=getConnection()
    sql='update account set CustomerName=%s,DateOfBirth=%s,Contact=%s,Address=%s where AccountNumber=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    
    db.commit()
    db.close()

def all():
    db=getConnection()
    sql="select * from account"
    cr=db.cursor()
    cr.execute(sql)
    row=cr.fetchall()
    db.commit()
    db.close()
    return row
##
##
##acc='123123'
##pasw='1234abcd'
##r=login()
##if (acc,pasw) in r:
##    print("y")
##else:
##    print("n")
