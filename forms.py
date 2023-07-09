from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddCupcakeForm(FlaskForm):
    flavor = StringField("Flavor", validators=[InputRequired()])
    rating = IntegerField("Rating", validators=[InputRequired(), NumberRange(min=1,max=10)])
    size = SelectField("Size", validators=[InputRequired()], choices=[('large','Large'),('medium','Medium'),('small','Small')])
    image = StringField("Image", validators=[Optional()])