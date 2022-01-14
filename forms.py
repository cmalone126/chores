from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired
from dbops import DBSimple
from operator import itemgetter

class NewChoreForm(FlaskForm):
    #nickNameList = list(map(itemgetter('nickname'), DBSimple.nicknames()))
    nickNameList = DBSimple.nicknames()
    choreName = StringField('Chore Name', \
            validators=[DataRequired(message='Chore Name Required')])
    choreDescription = StringField('Chore Description')
    #person = SelectField(label='Person', choices=nickNameList)
    #dateAssigned = DateField('Due Date', widget = DateTimePickerWidget)
    submit = SubmitField('Submit')

