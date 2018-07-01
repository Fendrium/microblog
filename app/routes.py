from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'charlie'}
    posts = [
        {
            'author': {'username': 'charlie'},
            'body': 'I like chocolate!'
        },
        {
            'author': {'username': 'Dante'},
            'body': 'I am ugly'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
