from flask import flash
from flask import redirect
from flask.templating import render_template
from pymysql.err import IntegrityError
from werkzeug.security import generate_password_hash

from app import app, db
from app.forms import SignupForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', user={'name': 'Jack'})


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        cursor = db.cursor()
        try:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                           (form.username.data, form.email.data, generate_password_hash(form.password.data)))
            db.commit()

            flash('Hello %s' % form.username.data)
            return redirect('/')
        except IntegrityError:
            flash('Duplicate Username!')

    return render_template('signup.html', form=form)
