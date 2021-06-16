from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

class UserCheck:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = 'Please choose another username'
        self.message = message
    
    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)
        
class myForm(FlaskForm):
    username = StringField('Username', validators = [ DataRequired(), UserCheck(message="custom rejection message", banned =['root','sys','admin']), Length(min=2,max=15)])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        if not username.data.isalpha():
            raise ValidationError("No special characters, please. Alphanumeric only")

@app.route('/', methods = ['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form=form, username=username)
    else:
        return render_template('home.html', form =form, username = "")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')