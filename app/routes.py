from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, NewToDoForm
from app.models import Users, ToDos, Comments
from app import app, db, login

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    if current_user.is_anonymous:
        return render_template("index.html", title="Home")
    if current_user.is_authenticated:
        todos = current_user.own_todos()
        return render_template("index.html", title="Home", items=todos)

@login.user_loader
def load_user(ID_User):
    return Users.query.get(int(ID_User))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(Username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('index'))
    return render_template("login.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(Username=form.username.data, Givenname=form.givename.data, Surname=form.surname.data, Mail=form.mail.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route("/new", methods=['GET', 'POST'])
@login_required
def new():
    form = NewToDoForm()
    if form.validate_on_submit():
        todo = ToDos(Name=form.name.data, Description=form.description.data, Status=form.status.data, Date=form.date.data, User_ID=current_user.ID_User)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("new.html", title='New ToDo', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/all", methods=['GET', 'POST'])
@login_required
def all():
    todos = current_user.all_todos()
    return render_template("all.html", title="All ToDos", items=todos)