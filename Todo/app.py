from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:doofus@34.89.51.129:3306/todo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db =SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140), nullable = False)
    date_added = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default = False)

@app.route('/')
def home():
    return "This is a Todo App"

@app.route('/add')
def add():
    return "Add a new Todo"

if __name__ == '__main__':
    app.run(debug= True, host = '0.0.0.0')