from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
app = Flask(__name__)
#mysql connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Bro@0066"
app.config["MYSQL_DB"]="user"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)
# app.config['SECRETE_KEY']=
#loading home page
@app.route("/")
def valid():
    con=mysql.connection.cursor()
    sql="Select * From student"
    con.execute(sql)
    res=con.fetchall()
    
    return render_template("table.html",datas=res)
# new user
@app.route("/index",methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['fname']
        rollno=request.form['roll']
        mail=request.form['mail']
        phone = request.form['phone']
        dept = request.form['dept']
        degree = request.form['degere']
        gender=request.form['gender']
        con=mysql.connection.cursor()
        sql="insert into student(fname,rollno,email,phno,dept,degree,gender) values(%s,%s,%s,%s,%s,%s,%s)"
        con.execute(sql,[name,rollno,mail,phone,dept,degree,gender])
        mysql.connection.commit()
        con.close()
        # flash('USER DETAILS ADDED')
        
        return redirect(url_for("valid"))
    return render_template("index.html")

@app.route("/update/<string:id>",methods=['GET','POST'])
def update(id):
    con = mysql.connection.cursor()
    if request.method=='POST':
       name=request.form['fname']
       rollno=request.form['roll']
       mail=request.form['mail']
       phone = request.form['phone']
       dept = request.form['dept']
       degree = request.form['degere']
       gender=request.form['gender']
       sql="update student set fname=%s,rollno=%s,email=%s,phno=%s,dept=%s,degree=%s,gender=%s where ID=%s"
       con.execute(sql,[name,rollno,mail,phone,dept,degree,gender,id])
       mysql.connection.commit()
       con.close()
       # flash('USER DETAILS UPDATED')
       
       return redirect(url_for("valid"))
       con = mysql.connection.cursor()

    sql = "select * from student where ID=%s"
    con.execute(sql,[id])
    res = con.fetchone()
    return render_template("edit.html", datas=res)
@app.route("/delete/<string:id>",methods=['GET','POST'])
def delete(id):
    con = mysql.connection.cursor()
    sql = "delete from student where ID=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    # flash('USER DETAILS DELETED')
    return redirect(url_for("valid"))
if __name__ == '__main__':
    app.run(debug=True)
