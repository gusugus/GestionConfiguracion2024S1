from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Base, Author, Book
from database import db
from forms import AuthorForm, BookForm

app = Flask(__name__) 

# Configuración de la clave secreta para la protección CSRF
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Configura la base de datos 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Crea las tablas en la base de datos
with app.app_context():
    db.create_all()

# Ruta para mostrar el formulario para agregar un nuevo autor
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    form = AuthorForm()

    if form.validate_on_submit():
        author_name = form.author_name.data
        new_author = Author(name=author_name)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('show_authors'))

    return render_template('add_author.html', form=form)

# Ruta para mostrar todos los autores
@app.route('/')
def show_authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)

# Define la ruta para borrar un autor
@app.route('/delete_author/<int:author_id>', methods=['GET'])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('show_authors'))

# Ruta para agregar un libro
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author_id = form.author.data
        author = Author.query.get_or_404(author_id)
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('show_books'))
    return render_template('add_book.html', form=form)




@app.route('/show_books')
def show_books():
    # Obtener todos los libros de la base de datos
    books = Book.query.all()
    
    # Renderizar la plantilla 'books.html' con los datos de los libros
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
