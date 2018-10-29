from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG']= True



@app.route("/")
def index():
    template = jinja_env.get_template('welcome.html')
    return template.render(username="", password="",verify_password="", email="", username_error = "",
    password_error="", verify_error="", email_error="")
    

def char_in_email(email):
    sum= 0
    main_email=email.split('@')[0]
    for char in main_email:
        sum+=1
    return (sum)

def dot_in_email(email):
    dot=0
    for i in email:
        if i==".":
            dot+=1
    return int(dot)

def at_in_email(email):
    at=0
    for i in email:
        if i=="@":
            at+=1
    return int(at)

@app.route("/welcome", methods=['POST'])
def welcome():
   username = request.form['username']
   password = request.form['password']
   verify_password =request.form['verify_password']
   email = request.form['email']
   username_error=""
   password_error=""
   verify_error=""
   email_error=""

   


   if username=="":
       username_error="Username field is empty"
   elif len(username)<3 or len(username)>20 or " " in username:
       username_error="Username is not valid. Range(3-20) and NO space"
       

   if password=="":
       password_error="Password field is empty"
   elif len(password)<3 or len(password)>20 or " " in password:
       password_error="Password is not valid. Range(3-20) and NO space" 
       password=""
       

   if verify_password=="":
       verify_error="Verify password field is empty" 
   elif not verify_password== password:
       verify_error= "Password did not match"
       verify_password=""


   #if len(char_in_email(email))<3 or len(char_in_email(email))>20 or not dot_in_email(email)==1 or not at_in_email(email)==1:
   if char_in_email(email)<3 or char_in_email(email)>20 or not dot_in_email(email)==1 or not at_in_email(email)==1 or " " in email:
       email_error= "Invalid Email"
    

   #RE-RENDER FORM IF ANY FIELD IS EMPTY.
   #if username=="" or password=="" or verify_password=="" or len(username)<3 or len(username)>20:
   if not username_error and not password_error and not verify_error and not email_error:
       return "<h1>" + "Welcome "+ username+"!</h1>"
   else:
       password=""
       verify_password=""
       template = jinja_env.get_template('welcome.html')
       return template.render(username=username, password=password,verify_password=verify_password, email=email, 
            username_error = username_error, password_error=password_error, verify_error=verify_error,
            email_error=email_error)
       
   

app.run()