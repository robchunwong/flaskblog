from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, AForm
from app.models import User, Post

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = AForm()
	users = User.query.all()
	return render_template('index.html', title='Home', users=users, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
