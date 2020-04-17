from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class userinput(FlaskForm):
    username1=StringField('First Username', validators=[DataRequired(), Length(min=2, max=20)])
    username2=StringField('Second Username', validators=[DataRequired(), Length(min=2, max=20)])
    submit=SubmitField('Compare')
