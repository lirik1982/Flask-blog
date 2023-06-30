from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask import flash, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = '7904b61c663dc3a7e6c868e1450d7a9a'

posts = [
    {
        'author': 'Kirill Degtyarev',
        'title': 'Blog Post 1',
        'content': "First post content",
        'date_posted': 'June 26, 2023',
    },
      {
        'author': 'Vlad Putin',
        'title': 'Blog Post 2',
        'content': "Second post content",
        'date_posted': 'June 28, 2023',
    },
       {
        'author': 'Jo Biden',
        'title': 'Blog Post 3',
        'content': "3 post content",
        'date_posted': 'June 29, 2023',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@ya.ru' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)