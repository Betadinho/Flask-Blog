from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


class RegistrationForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

        email = StringField('Email', validators=[DataRequired(), Email()])

        password = StringField('Password', validators=[DataRequired()])

        confirm_password = StringField('Confirm password', validators=[DataRequired(), EqualTo('password')])

        submit = SubmitField('Sign Up')

        def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken. Please choose a different one.')
        
        def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already taken. Please use a different one.')

class LoginForm(FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Email()])

        password = StringField('Password', validators=[DataRequired()])

        remember = BooleanField('Remember me')

        submit = SubmitField('Login')
