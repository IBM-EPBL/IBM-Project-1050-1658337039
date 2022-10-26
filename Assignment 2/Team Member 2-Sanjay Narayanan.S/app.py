from flask import Flask,render_template, request,jsonify
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup',methods = ['POST', 'GET'])
def signup():
    return render_template('signup.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
         email = request.form['email']
         password = request.form['password']

         con=sql.connect("user_database.db")
         cur = con.cursor()
         statement=f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}';"
         cur.execute(statement)
         if not cur.fetchone():
            msg = "invalid email or password",
         else:
            msg = "login successfully"
   return render_template('home.html',msg=msg)
   con.close()

@app.route('/adduser',methods = ['POST', 'GET'])
def adduser():
   if request.method == 'POST':
      try:
         name = request.form['name']
         email = request.form['email']
         password = request.form['password']
         confirm_password = request.form['confirm_password']
         
         with sql.connect("user_database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (name,email,password,confirm_password) VALUES (?,?,?,?)",(name,email,password,confirm_password) )
            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return msg
         con.close()

if __name__ == '__main__':
   app.run(debug=True)