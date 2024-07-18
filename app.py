from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("login1.html")
database={'Ram':'Ram@123','Raj':'Raj@123','Ravi':'Ravi@123'}
@app.route('/form_login',methods=['POST','GET'])
def  form_login():
    if request.method=='POST':
        name1=request.form['username']
        password1=request.form['password']
        if name1 not in database:
            return render_template('login1.html',info="Invalid user")
        else:
            if database[name1]!=password1:
                return render_template('login1.html',info="Invalid password")
            else:
                return render_template('home1.html',name=name1)
    return render_template('login1.html')
if __name__=="__main__":
    app.run(debug=True)