from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:27724369@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://cszaopzvluopdt:4bf11e1d17d1c8d48e85d7a9a974ddbb3ce33c51f3f79c259a6d3406295ee822@ec2-18-211-41-246.compute-1.amazonaws.com:5432/dcl3ll35gttlis'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods = ['post'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    
    return redirect(url_for('index'))









# nota
# usa o cmd pra ativar 
# scripts\activate
# o resto da ativação vc lembra hehe

# @app.route('/')
# def index():
#     # return '<h1> Hello World! </h1>'
#     fruits = ["apple", "grapes", "berries", "oranges"]
#     return render_template('index.html', kote='Kindness needs no translation', fruits = fruits)

    
# @app.route('/about')
# def about():
#     return '<h1> Hello World from about page</h1>'


# @app.route('/quotes')
# def quotes():
#     return '<h1> Life is a journey</h1>'

