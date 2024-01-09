#app/job/routes.py

from flask          import render_template, redirect, url_for, flash, request
from flask_login    import login_required, current_user
from app.models     import Job, Firma
from .              import job
from .forms         import CreateJobForm
from app            import db

# Jobs anzeigen
@job.route('/jobs')
@login_required
def list_jobs():
    jobs = Job.query.all()
    return render_template('job.html', title='Jobs', jobs=jobs)


# Job erstellen
@job.route('/create_job', methods=['GET', 'POST'])
@login_required
def create_job():
    form = CreateJobForm() 
    if current_user.is_authenticated and current_user.is_firma:
        if form.validate_on_submit():
            if isinstance(current_user, Firma):
                job = Job(
                    stellenbezeichnung      = form.stellenbezeichnung.data,
                    qualifikationen         = form.qualifikationen.data,
                    standort                = form.standort.data,
                    arbeitszeit             = form.arbeitszeit.data,
                    vertrag                 = form.vertrag.data,
                    vergütung               = form.vergütung.data,
                    bewerbungsfrist         = form.bewerbungsfrist.data,
                    kontaktinformationen    = form.kontaktinformationen.data,
                    stellenbeschreibung     = form.stellenbeschreibung.data,
                    name                    = current_user.name
                )
                db.session.add(job)
                db.session.commit()
                flash('Job erfolgreich erstellt!')
                return redirect(url_for('job.list_jobs'))
        else:
            print("ungültig", form.errors)
    return render_template('create_job.html', title='Job erstellen', form=form)

# Job folgen
@job.route('/follow_job/<int:job_id>')
@login_required
def follow_job(job_id):
    job = Job.query.get(job_id)
    if job:
        if current_user not in job.followers_users_job:
            job.followers_users_job.append(current_user)
            db.session.commit()
            flash('Sie folgen jetzt diesem Job!')
        else:
            flash('Sie folgen diesem Job bereits!')
    else:
        flash('Job nicht gefunden.', 'error')
    return redirect(url_for('job.list_jobs'))