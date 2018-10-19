from flask import Flask, request, redirect, render_template
import cgi, re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    return render_template('signup_form.html')


@app.route("/signup", methods=['POST'])
def signup_form():
    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']
 
    
    reg = re.compile(r"[^ \t\n\r\f\v]{3,20}")
    reg_email1 = re.compile(r"[^ \t\n\r\f\v@]*@[^ \t\n\r\f\v@]*")
    reg_email2 = re.compile(r"[^ \t\n\r\f\v\.]*\.[^ \t\n\r\f\v\.]*")
    #Validation for Username
    error_username = ''
    #if " " in username or len(username) < 3 or len(username) > 20: 
    if not reg.fullmatch(username):
        error_username = "That's not a valid username"  
  
        username = ''

    #Validation for Password
    error_password = ''
    if not reg.fullmatch(password):
        error_password = "That's not a valid password"

    #Validation for Verify Password
    error_v_password = ''
    if not v_password or (v_password != password): 
        error_v_password =  "Passwords don't match"

    #Validation for Email   
    error_email = ''
    if email:
        if not reg.fullmatch(email) or not reg_email1.fullmatch(email) or not reg_email2.fullmatch(email):
            error_email = "That's not a valid email" 
            email = ''

    if error_username or error_password or error_v_password or error_email:
        return render_template('signup_form.html', 
            username = username,
            email = email,
            error_username=error_username,
            error_password=error_password,
            error_v_password=error_v_password,
            error_email=error_email)
    else:
        return render_template('welcome.html', username=username )

app.run()