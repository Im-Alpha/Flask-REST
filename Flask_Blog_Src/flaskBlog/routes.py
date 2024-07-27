from flask import render_template, jsonify, url_for, flash, redirect
from flaskBlog import app
from flaskBlog.forms import RegistrationForm, LoginForm
# Move model import after db is initialized to avoid errors
from flaskBlog.models import User, Post

posts =[
    {
        'author': 'Jacob Delgado',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 16, 2024'
    },
    {
        'author': 'Keiwa on the Kob',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 18, 2024'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    # return jsonify({ 
    #     'author': 'Jacob Delgado',
    #     'title': 'Blog Post 1',
    #     'content': 'First post content',
    #     'date_posted': 'April 16, 2024'})

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect Login information', 'danger')
    return render_template('login.html', title='Login', form=form)
