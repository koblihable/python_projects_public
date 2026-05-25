from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import String, Float, Integer, desc
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import requests
import os

# URL and API token for movie search
MOVIES_URL = 'https://api.themoviedb.org/3/search/movie'
API_TOKEN = os.environ.get('API_TOKEN')

# api header
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ.get('API_TOKEN')}"
}

# token for WTForms
SECRET_KEY = os.environ.get('SECRET_KEY')

# setting up db
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

# setting up flask application and updating config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///films.db'
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)

# database tables
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(255), default='No description')
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(400), default='No review')
    img_url: Mapped[str] = mapped_column(String(255), nullable=False)

with app.app_context():
    db.create_all()

# flask forms definitions
class EditForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review')
    submit = SubmitField('Edit Movie')

class AddForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

bootstrap = Bootstrap5(app)

# flask paths setup
@app.route('/')
def home():
    result = db.session.execute(db.select(Movie).order_by(desc(Movie.rating)))
    movies = result.scalars().all()
    for ranking, movie in enumerate(movies, start=1):
        movie.ranking = ranking
    db.session.commit()
    result = db.session.execute(db.select(Movie))
    movies_to_display = result.scalars().all()
    return render_template('index.html', movies=movies_to_display)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        movie_to_update = db.get_or_404(Movie, id)
        movie_to_update.rating = request.form.get('rating')
        movie_to_update.review = request.form.get('review')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form)

@app.route('/delete/<int:id>')
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('index.html'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        url = 'https://api.themoviedb.org/3/search/movie'
        movie = request.form.get('title')
        params = {
            'include_adult': 'false',
            'language': 'en-US',
            'query': movie
        }
        response = requests.get(url, headers=headers, params=params)
        movies = response.json()['results']
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=add_form)

@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/search/<int:id>', methods=['GET', 'POST'])
def search_and_add(id):
    url = f'https://api.themoviedb.org/3/movie/{id}'
    response = requests.get(url, headers=headers).json()
    movie = Movie(title=response['title'],
                  year=response['release_date'][:4],
                  description=response['overview'],
                  rating=round(response['vote_average'],1),
                  review='None',
                  img_url=f'https://image.tmdb.org/t/p/original/{response["poster_path"]}')
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('edit', id=movie.id))

if __name__ == "__main__":
    app.run(debug=True)