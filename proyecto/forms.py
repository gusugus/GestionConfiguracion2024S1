from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from models import Author

class AuthorForm(FlaskForm):
    author_name = StringField('Nombre del Autor', validators=[DataRequired()])
    submit = SubmitField('Agregar Autor')

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = SelectField('Author', coerce=int, validators=[DataRequired()], choices=[])
    submit = SubmitField('Add Book')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.author.choices = [(author.id, author.name) for author in Author.query.all()]