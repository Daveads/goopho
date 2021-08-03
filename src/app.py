import click
from goopho import app
from datetime import datetime

#models instant
from goopho import User, setRole
from goopho import db
from goopho import create_root

if __name__ == "__main__":

    root = create_root()
    if root:
        
        print(" * root created see doc for details")

    app.run()



@app.cli.command()
def test():
    click.echo(" * i am test")


@app.cli.command()
def run():

    if __name__ == "__main__":
        root = create_root()

        if root:

            print(" * root created see doc for details")

        app.run()
        


@app.cli.command()
def root():
    "creates a root user"
    root = create_root()

    if root:
        
        print(" * root created see doc for details")


@app.cli.command()
def dbinit():
    "This initiate the database tables"
    from goopho import db
    db.create_all()
    print("* Database initiated")


#help()

@app.cli.command()
def goopho():
    'help from goohpo'

    print("#migration")

    print("**for first migration**")
    print("flask db init")
    print("flask db migrate -m 'Initial migration.' ")
    print("flask db upgrade")