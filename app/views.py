from app import app, mail
from flask import render_template, redirect, url_for
from flask.ext.mail import Message
from forms import ContactForm


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print u'Validated form'
        subject = form.subject.data
        body = """Message from {name} ({email}),\n\n{message}""".format(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        sender = (form.name.data, form.email.data)
        recipients = ['imauld@gmail.com']
        msg = Message(
            subject=subject,
            body=body,
            sender=sender,
            recipients=recipients
        )
        mail.send(msg)
        return redirect(url_for('contact'))
    else:
        print u'Something went wrong'
    return render_template('contact.html', form=form)