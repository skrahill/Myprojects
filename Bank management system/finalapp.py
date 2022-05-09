from flask import *

from fdbm import *



app = Flask(__name__)

#loginpage
@app.route("/")
def home():
    return render_template("flogin.html")

#newaccount
@app.route("/newacc")
def new_acc():
    return render_template("newacc.html")

@app.route("/selectall",methods=["POST"])
def details_page():
    acc=request.form["accno"]
    a=(acc)
    data=selectall(a)
    return render_template("details.html",elist=data)

@app.route("/editEmp")
def edit_emp():
    acc=request.args.get("accno")
    t=(acc)
    data=selectbyaccno(t)
    return render_template("edit.html",row=data)

@app.route("/updateemp", methods=["POST"])
def update_emp():
    acc= request.form["accno"]
    name = request.form["cname"]
    contact = request.form["contact"]
    adress= request.form["address"]
    dob=request.form["dob"]
    

    t = ( name,dob,contact,adress,acc)
    update(t)
    return redirect("/accno")

@app.route("/deleteEmp")
def delete_emp():
    acc=request.args.get("accno")
    deleteEmp(acc)
    return redirect("/") 

@app.route("/withdraw",methods=["POST"])
def withdraw_amt():
    w=1
    acc=request.form["accno"]
    widamt=int(request.form["widamt"])
    w=withdraw(widamt,acc)
    if w == 0:
        return render_template("widelse.html")
    else:
        
        return render_template("widamt.html")
   
@app.route("/withdrawamt")
def with_amt():
    return render_template("withdraw.html")

@app.route("/deposite",methods=["POST"])
def deposite_amt():
    acc=request.form["accno"]
    depamt=int(request.form["depamt"])
    deposite(depamt,acc)
    return redirect("/depamt")

@app.route("/depositeamt")
def dep():
    return render_template("deposite.html")
@app.route("/depamt")
def dep_amt():
    return render_template("depamt.html")
    

@app.route("/adduser", methods=["POST"])
def add_user():
    cname=request.form["cname"]
    Accno = request.form["accno"]
    DOB = request.form["dob"]
    Contact = request.form["contact"]
    Adress = request.form["address"]
    balance = request.form["balance"]

    t = (cname,Accno,DOB,Contact,Adress,balance)
    adduser(t)
    return redirect("/")

@app.route("/accno")
def acc_no():
    return render_template("/accno.html")


@app.route("/welcome")
def trans():
    return render_template("mainpage.html")

@app.route("/login",methods=["post"])
def login_page():
    acc= request.form["accno"]
    password = request.form["cname"]
    
    
    res=login()
    if (acc,password) in res:
        
        return redirect("/welcome")
    else:
        return redirect("/")



































if(__name__=="__main__"):
    app.run(debug=True)
