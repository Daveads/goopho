import click
from goopho import app
from goopho import User
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

    user = User.query.filter_by(username=['goopho']).first()
    
    print(user)

    """
    if user:

        print("user already exist")

    else:

        new_user = User(name="Goopho Root", username="goopho", email="the.goopho@gmail.com", password="123456", roles="Admin")

        db.session.add(new_user)
        db.session.commit()

        print("Root user created !!!!")

    """
