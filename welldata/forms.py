from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class SignupForm(FlaskForm):
    """ User signup form. """

    username = StringField(
        'Username',
        validators=[DataRequired(message='Enter your username.')]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Please enter your password.'),
            Length(min=6, message='Password must be at least 6 characters.'),
            EqualTo('confirm', message='Password must match.')
        ]
    )
    confirm = PasswordField('Confirm your password',)
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """ User login form. """

    username = StringField(
        'Username',
        validators=[DataRequired(message='Please enter your username.')]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message='Please enter your password.')]
    )
    submit = SubmitField('Login')
