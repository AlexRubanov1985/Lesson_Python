import os

from flask import Flask, render_template, flash, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form3 = LoginForm()
    if form3.validate_on_submit():
        name = form3.username.data
        print(form3.pasword.data)
        print(form3.remember_me.data)

        flash('YES,' + name + ' Flash flask work!!')
        flash('YES, Flash flask work22!!')
        flash('YES, Flash flask work3333!!')
        return redirect('/')
    return render_template('login.html', form2=form3)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
