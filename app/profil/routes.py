#app/profil/routes.py

from flask          import render_template, redirect, url_for, flash, request
from flask_login    import login_required, current_user
from app.models     import User, Firma
from .              import profil
from .forms         import EditProfileForm, EditProfileFormF
from app            import db




#User Profil anzeigen
@profil.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)

#User Profil bearbeiten
@profil.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        if isinstance(current_user, User):
            current_user.username       = form.username.data
            current_user.about_me       = form.about_me.data
            current_user.vorname        = form.vorname.data
            current_user.nachname       = form.nachname.data
            current_user.alter          = form.alter.data
            current_user.beruf          = form.beruf.data
            current_user.qualifikation  = form.qualifikation.data
        
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('profil.edit_profile'))
    elif request.method == 'GET':
        form.username.data          = current_user.username
        form.about_me.data          = current_user.about_me
        form.vorname.data           = current_user.vorname
        form.nachname.data          = current_user.nachname
        form.alter.data             = current_user.alter
        form.beruf.data             = current_user.beruf
        form.qualifikation.data     = current_user.qualifikation
        
    return render_template('edit_profile.html', title='Edit Profile', form=form)


# Firmen Profil anzeigen
@profil.route('/profilef/<fusername>')
def profilef(fusername):
    firma = Firma.query.filter_by(fusername=fusername).first_or_404()
    return render_template('profilef.html', firma=firma)


# Firmen Profil bearbeiten
@profil.route('/edit_profilef', methods=['GET', 'POST'])
@login_required
def edit_profilef():
    form = EditProfileFormF(current_user.fusername)
    if form.validate_on_submit():
        if isinstance(current_user, Firma):
            current_user.fusername      = form.fusername.data
            current_user.name           = form.name.data
            current_user.rechtsform     = form.rechtsform.data
            current_user.sitz           = form.sitz.data
            current_user.leitung        = form.leitung.data
            current_user.mitarbeiterzahl= form.mitarbeiterzahl.data
            current_user.umsatz         = form.umsatz.data
            current_user.branche        = form.branche.data

        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('profil.edit_profilef'))
    elif request.method == 'GET':
        form.fusername.data         = current_user.fusername
        form.name.data              = current_user.name
        form.rechtsform.data        = current_user.rechtsform
        form.sitz.data              = current_user.sitz
        form.leitung.data           = current_user.leitung
        form.mitarbeiterzahl.data   = current_user.mitarbeiterzahl
        form.umsatz.data            = current_user.umsatz
        form.branche.data           = current_user.branche

    return render_template('edit_profilef.html', title='Edit Firm Profile', form=form)
