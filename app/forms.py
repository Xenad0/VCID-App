from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import Users

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    givename = StringField('Givenname', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordcheck = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Users.query.filter_by(Username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_mail(self, mail):
        user = Users.query.filter_by(Mail=mail.data).first()
        if user is not None:
            raise ValidationError('Please use a different mail.')
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NewToDoForm(FlaskForm):
    name = StringField('Titel', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    status = SelectField('Status', choices=[('open','Open'),('work','Working'),('wait','Waiting')], validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Create')