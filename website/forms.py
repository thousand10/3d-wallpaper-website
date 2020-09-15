from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Contact_us(FlaskForm):
    username = StringField('Your Name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    content = TextAreaField('message',validators=[DataRequired()])
    submit = SubmitField('send')