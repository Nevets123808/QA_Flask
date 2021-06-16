from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from os import getenv

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

class BasicForm(FlaskForm):
    first_name = StringField('First Name:')
    last_name = StringField('Last Name:')
    dob = DateField('Date of Birth:')
    age = IntegerField('Age:')
    colour = SelectField('Favourite Colour:',choices=[('#ff0000','red'),('#00ff00','green'),('#0000ff','blue')])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        colour = "color:"+form.colour.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last names."
        else: 
            return f'<p style=\"{colour}\";>thank you, {first_name} {last_name}.</p>'
    
    return render_template('home.html', form = form, message = error)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')