import click
from goopho import app
from datetime import datetime

#models instant
from goopho import User, setRole

from goopho import db


"""
if __name__=="__main__":
    app.run()
"""


@app.cli.command()
def test():
    click.echo("i am test")


@app.cli.command()
def run():

    if __name__ == "__main__":

        app.run()


@app.cli.command()
def root():
 
    user = User.query.filter_by(username="goopho").first()

    if user:

        print("user already exist")

    else:
        
        datenow = datetime.now()

        date = datenow.strftime("%d/%m/%Y %H:%M:%S")
        
        new_user = User(name="Goopho", username="goopho", email="the.goopho@gmail.com", password="123456", roles=setRole.admin, email_verification=date)

        db.session.add(new_user)
        db.session.commit()

        print("Root user created !!!!")
        print("Email : the.goopho@gmail.com")
        print("Password : 123456")
