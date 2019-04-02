from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Book(db.Model):
    __tablename__ = 'Book'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    autor = db.Column(db.String(40), nullable=False)


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book

    nome = fields.Str(required=True)
    autor = fields.Str(required=True)


db.create_all()

@app.route('/', methods=['GET'])
def home():
    return 'Olá jovens'


@app.route('/oi/<user>', methods=['GET'])
def oi(user):
    return f'Olá {user}'


@app.route('/create-book', methods=['POST'])
def create_book():
    bs = BookSchema()
    book, error = bs.load(request.json)
    if error:
        return jsonify(error), 400

    db.session.add(book)
    db.session.commit()
    return bs.jsonify(book), 201
