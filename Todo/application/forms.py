from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TodoForm(FlaskForm):
    task_name = StringField('Task name: ',validators = [DataRequired(), Length(min=3,max=140)])
    submit = SubmitField('Add Task')