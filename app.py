from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ebooks.db'
db = SQLAlchemy(app)

class Ebook(db.Model):

    #booktitle + "," + booklink + "," + bookprice + "," + imglink +"\n"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(300), nullable=False)
    title = db.Column(db.String(300), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    coverlink = db.Column(db.String(200), nullable=True)
    source = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    books = Ebook.query.order_by(Ebook.author).all()
    return render_template('index.html', books=books)


@app.route('/process', methods=['POST', 'GET'])
def process():
    
    with open("ebooks.txt", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    

    for line in lines:

        data = line.split("|")

        new_book = Ebook(author=data[0],title=data[1],link=data[2],price=data[3],coverlink=data[4],source=data[5])

        try:
            db.session.add(new_book)
            db.session.commit()

        except:
            pass

    return 'DONE'

if __name__ == "__main__":
    app.run(debug=True)