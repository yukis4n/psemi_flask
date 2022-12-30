from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

#if __name__ == "__main__":
    #app.run()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///smaple.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Sample_db(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),nullable=False)

if __name__ == "__main__":
    db.create_all()
    #app.run()