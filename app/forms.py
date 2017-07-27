from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class NewProjectForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    shortDescription = TextAreaField('ShortDescription', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])


