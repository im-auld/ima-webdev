from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import Required, Email

REQUIRED = 'This is a required field'

class ContactForm(Form):
    name = TextField('Name', validators = [Required('This is a required field')])
    email = TextField('Email', validators = [Required('This is a required field'), Email('Please enter a valid email address')])
    subject = TextField('Subject', validators = [Required('This is a required field')])
    message = TextAreaField('Message', validators = [Required('This is a required field')])
    submit = SubmitField('Send')