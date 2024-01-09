#app/profil/forms.py

from flask_wtf          import FlaskForm
from wtforms            import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models         import User, Firma

#User Profil editieren
class EditProfileForm(FlaskForm):
    username        = StringField('Username', validators=[DataRequired()])
    vorname         = StringField('Vorname', validators=[Length(max=64)])
    nachname        = StringField('Nachname', validators=[Length(max=64)])
    alter           = IntegerField('Alter')
    beruf           = StringField('Beruf', validators=[Length(max=64)])
    qualifikation   = StringField('Qualifikation', validators=[Length(max=64)])
    about_me        = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit          = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class EditProfileFormF(FlaskForm):
    fusername       = StringField('Firmenname', validators=[DataRequired()])
    name            = StringField('Name', validators=[Length(max=64)])
    rechtsform      = StringField('Rechtsform', validators=[Length(max=64)])
    sitz            = StringField('Sitz')
    leitung         = StringField('Leitung', validators=[Length(max=64)])
    mitarbeiterzahl = IntegerField('Mitarbeiterzahl')
    umsatz          = StringField('Umsatz', validators=[Length(max=64)])
    branche         = StringField('Branche', validators=[Length(max=64)])
    submit          = SubmitField('Submit')

    def __init__(self, original_fusername, *args, **kwargs):
        super(EditProfileFormF, self).__init__(*args, **kwargs)
        self.original_fusername = original_fusername

    def validate_fusername(self, fusername):
        if fusername.data != self.original_fusername:
            firma = Firma.query.filter_by(fusername=fusername.data).first()
            if firma is not None:
                raise ValidationError('Please use a different firm name.')