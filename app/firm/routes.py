#app/firm/routes.py

from flask          import render_template, redirect, url_for, flash
from flask_login    import login_required, current_user
from app.models     import Firma
from .              import firm

#Firmenliste
@firm.route('/firma')
@login_required
def list_firmen():
    if current_user.is_authenticated:
        firmen = Firma.query.all()
        return render_template('firmen.html', title='Liste der Firmen', firmen=firmen)
    else:
        flash('Nur angemeldete Firmen können diese Seite sehen.', 'warning')
        return render_template('firmen.html', title='Firmen', form=form)