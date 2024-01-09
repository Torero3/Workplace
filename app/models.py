# app/models.py

from app            import db, login
from flask_login    import UserMixin
from flask          import session

@login.user_loader
def load_user(id):
    table = session.get("_table")
    if table == "User":
        return User.query.get(int(id))
    else: 
        return Firma.query.get(int(id))


# class FirmFollower(db.Model):
#     __tablename__           = "firm_followers"
#     id                      = db.Column(db.Integer, primary_key=True)
#     follower_id             = db.Column(db.Integer, db.ForeignKey('users.id'))
#     followed_id             = db.Column(db.Integer, db.ForeignKey('firma.id'))

# class JobFollower(db.Model):
#     __tablename__           = "job_followers"
#     id                      = db.Column(db.Integer, primary_key=True)
#     user_id                 = db.Column(db.Integer, db.ForeignKey('users.id'))
#     job_id                  = db.Column(db.Integer, db.ForeignKey('jobs.id'))

user_follows = db.Table('user_follows',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('firma_id', db.Integer, db.ForeignKey('firma.id'), primary_key=True),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__           = "user"
    id                      = db.Column(db.Integer, primary_key=True)
    username                = db.Column(db.String(64), index=True, unique=True)
    password_hash           = db.Column(db.String(255))
    email                   = db.Column(db.String(120), index=True, unique=True)
    vorname                 = db.Column(db.String(64))
    nachname                = db.Column(db.String(64))
    alter                   = db.Column(db.Integer)
    beruf                   = db.Column(db.String(64))
    qualifikation           = db.Column(db.String(64))
    about_me                = db.Column(db.Text())
    # followed_firmen         = db.relationship('Firma', secondary='firm_followers', backref=db.backref('followers_users_f', lazy='dynamic'), lazy='dynamic')
    # followed_jobs           = db.relationship('Job', secondary='job_followers', backref=db.backref('followers_users_j', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def get_id(self):
        return str(self.id)


class Firma(db.Model, UserMixin):
    __tablename__           = "firma"
    id                      = db.Column(db.Integer, primary_key=True)
    fusername               = db.Column(db.String(64), index=True, unique=True)
    fpassword_hash          = db.Column(db.String(255))
    femail                  = db.Column(db.String(120), index=True, unique=True)
    name                    = db.Column(db.String(64), unique=True)                 # es kann immer nur eine Firma geben
    rechtsform              = db.Column(db.String(64))
    sitz                    = db.Column(db.String(64))
    leitung                 = db.Column(db.String(64))
    mitarbeiterzahl         = db.Column(db.Integer)
    umsatz                  = db.Column(db.String(64))
    branche                 = db.Column(db.String(64))
    is_firma                = db.Column(db.Boolean, default=True)
    # followers_users_firm    = db.relationship('User', secondary='firm_followers', backref=db.backref('followed_f', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Firma {}>'.format(self.fusername)

    def get_id(self):
        return str(self.id)


class Job(db.Model):
    __tablename__           = "job"
    id                      = db.Column(db.Integer, primary_key=True)
    stellenbezeichnung      = db.Column(db.String(64), index=True)
    qualifikationen         = db.Column(db.String(64))
    standort                = db.Column(db.String(64))
    arbeitszeit             = db.Column(db.String(64))
    vertrag                 = db.Column(db.String(64))
    vergütung               = db.Column(db.String(64))
    bewerbungsfrist         = db.Column(db.String(64))
    kontaktinformationen    = db.Column(db.String(64))
    submit                  = db.Column(db.String(64))
    cancel                  = db.Column(db.String(64))
    stellenbeschreibung     = db.Column(db.Text())
    firma_id                = db.Column(db.Integer, db.ForeignKey('firma.id'), unique=True)
    name                    = db.Column(db.String(64), unique=True)
    # firma                   = db.Column(db.Integer, db.ForeignKey('firma.name'), unique=True)
    # firma_id                = db.Column(db.Integer, db.ForeignKey('firma.id'), unique=True)
    # followers_users_job     = db.relationship('User', secondary='job_followers', backref=db.backref('followed_j', lazy='dynamic'), lazy='dynamic', overlaps="followed_jobs")