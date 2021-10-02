from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c52bb49d73b75d16255ff040b59a41a4'

posts = [
    {
        'author': 'Joseph Eshiett',
        'title': 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted':'October 2, 2021'
    },
    {
        'author': 'Joey Eshiett',
        'title': 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted':'October 3, 2021'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='about')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

