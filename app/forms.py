from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SelectField, validators
from wtforms.validators import DataRequired

from werkzeug.utils import secure_filename

class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    
    gender = SelectField('Gender', choices=[('male','Male'), ('female','Female')])
    
    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    
    biography = StringField('Biography', validators=[DataRequired()])
    
    
class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
    description = StringField('Description', validators=[DataRequired()])    