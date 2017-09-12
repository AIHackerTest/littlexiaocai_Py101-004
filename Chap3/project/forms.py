from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import BooleanField, StringField, PasswordField, validators

class WeatherForm(Form):
    city = StringField('city',[validators.Length(min=0, max=25)])


