# Übernommen aus den Beispielen
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import Users

# Übernommen aus den Beispielen
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # Eigenentwicklung
    givename = StringField('Givenname', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    # Übernommen aus den Beispielen
    mail = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordcheck = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Übernommen aus den Beispielen
    def validate_username(self, username):
        user = Users.query.filter_by(Username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    
    # Übernommen aus den Beispielen
    def validate_mail(self, mail):
        user = Users.query.filter_by(Mail=mail.data).first()
        if user is not None:
            raise ValidationError('Please use a different mail.')

# Übernommen aus den Beispielen        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Eigenentwicklung
class NewToDoForm(FlaskForm):
    name = StringField('Titel', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Open','Open'),('Doing','Doing'),('Waiting','Waiting')], validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Create')

# Eigenentwicklung
class NewUpdateForm(FlaskForm):
    titel = StringField('Titel', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')

# Eigenentwicklung
class EditToDoForm(FlaskForm):
    name = StringField('Titel', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Update')