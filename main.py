from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# This is where I set secret key
app.config['SECRET_KEY'] = '2feea2720d48bd16f90deb7fc68199e4'

posts = [
    {
        "author": "Ezeibe Uchechukwu",
        "title": "Blog post 1",
        "content": "First post contect",
        "date_posted": "November 9, 2023"
    },

    {
        "author": "Okoro Emeka",
        "title": "Blog post 2",
        "content": "Second post contect",
        "date_posted": "November 10, 2023"
    },

    {
        "author": "Jennifer Mark",
        "title": "Blog post 3",
        "content": "Third post contect",
        "date_posted": "November 11, 2023"
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About us')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # To check if the form is validate when submit is clicked
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '22222222':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)