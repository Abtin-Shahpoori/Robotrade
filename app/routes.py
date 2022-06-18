from app import app
import sys
from app.forms import LoginForm
from flask import request, render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
sys.path.append("../../bots")
# import manager

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': "Abtin"} 
    return render_template('index.html', title=user["username"], user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid username')
            return redirect(url_for('login'))
        
        if not user.check_password(form.password.data):
            flash('Invalid Password')
            return redirect(url_for('login'))
        
        login_user(user, remember=False)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', form=form)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/index/run-bot-<bot>')
def run_bot(bot):
    try:
        # manager.run(bot) 
        print("ANM")
    except:
        return "something went wrong"
