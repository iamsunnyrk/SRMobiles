
# import smtplib 
# import cgi
# from flask import request, redirect
@app.route('/sendemail', methods = ['POST'])
# form = cgi.FieldStorage()
# name =  form.getvalue('name')
# email=form.getvalue('email')
# body=form.getvalue('body')
# mobile=form.getvalue('mobile')
# print(form['name'].value)
# print(form['email'].value)

def sendemail():
    # email = request.form['email']
    print("The email address is")
    # return redirect('/index.html')

# s = smtplib.SMTP('smtp.gmail.com', 587) 

# # start TLS for security 
# s.starttls() 

# # Authentication 
# s.login("sunnysambyal15@gmail.com", "jxfnwnomelanrwlx") 

# sender = email
# receiver = "sunnysambyal15@gmail.com"

# # message to be sent 
# message = f"""\
# Subject: Hi Sunny
# To: {receiver}
# From: {sender}

# Name:"+Name+"\nMobile No:"+nMobile+"\nEnquiry:"+body"""

# # sending the mail 
# s.sendmail(email, receiver, message) 

# # terminating the session 
# s.quit() 
