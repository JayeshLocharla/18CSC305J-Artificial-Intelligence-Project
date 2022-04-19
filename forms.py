from ast import Str, Sub
from tokenize import String
from typing import Text
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class InputForm(FlaskForm):
    inputtext = TextAreaField('Enter  your text here', validators=[DataRequired(), Length(min=20, max=100000)])
    submit = SubmitField('Proceed')

class UploadFileForm(FlaskForm):
    file = FileField('Drag and Drop to Upload File', validators=[DataRequired(), FileAllowed(['txt', 'doc'])])
    submit = SubmitField('Proceed') 