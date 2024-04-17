from database import db
from sqlalchemy.orm import relationship


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f'<Author {self.name}>'