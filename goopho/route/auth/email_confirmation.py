

#@app.route(/email-confirmation, method=['POST']):
def email():
    pass
"""
token is send to the backend 

then check if token if valid and get the user public id and 

then

get email from the database

then send an email to the user email containing code


/email-confirmation/code
once the code is confirmed

user.confirmation = store current time
db.session.commit()
"""




# only confirmed email should be allow to upload 
