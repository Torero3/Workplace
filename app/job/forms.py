#app/job/forms.py

from flask_wtf          import FlaskForm
from wtforms            import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from app.models         import Job, Firma


class CreateJobForm(FlaskForm):
    stellenbezeichnung      = StringField('Stellenbezeichnung', validators=[DataRequired()])
    qualifikationen         = StringField('Qualifikationen', validators=[DataRequired()])
    standort                = StringField('Standort', validators=[DataRequired()])
    arbeitszeit             = StringField('Arbeitszeit', validators=[DataRequired()])
    vertrag                 = StringField('Vertrag', validators=[DataRequired()])
    vergütung               = StringField('Vergütung', validators=[DataRequired()])
    bewerbungsfrist         = StringField('Bewerbungsfrist', validators=[DataRequired()])
    kontaktinformationen    = StringField('Kontaktinformationen', validators=[DataRequired()])
    stellenbeschreibung     = TextAreaField('Stellenbeschreibung', validators=[DataRequired(), Length(min=10)])
    name                    = StringField('Firma')
    submit                  = SubmitField('Submit')