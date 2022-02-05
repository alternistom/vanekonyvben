from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ekonyv.db'
db = SQLAlchemy(app)

class ebooks(db.Model):

    #booktitle + "," + booklink + "," + bookprice + "," + imglink +"\n"

    eid = db.Column(db.Integer, primary_key=True, unique = True, nullable=False)
    author = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    webshoplink = db.Column(db.Text, nullable=False)
    source = db.Column(db.Text, nullable=False)
    webshopid = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    books = ebooks.query.order_by(ebooks.author, ebooks.title).all()
    return render_template('index.html', books=books)




if __name__ == "__main__":
    app.run(debug=True)