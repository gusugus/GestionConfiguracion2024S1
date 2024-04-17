from database import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey  # Importa ForeignKey desde SQLAlchemy


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'))  # Añadido ForeignKey
    author = relationship("Author", back_populates="books")
