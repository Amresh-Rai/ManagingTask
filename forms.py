from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description')
    due_date = DateField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], validators=[DataRequired()])
    remarks = TextAreaField('Remarks')
    user_name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=100)])
    user_id = StringField('Your ID', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Save Task')
