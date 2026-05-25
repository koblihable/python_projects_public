from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, TextAreaField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import os
import datetime as dt


# secret key for create form
#TODO sort this shit out
#SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'MPWcM6RfN/stL6+pk5f/XI2zbJM='

# database initialization
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

# update config
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db.init_app(app)

ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)

# create a model for blog post
class BlogPost(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    subtitle:Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    body:Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    date:Mapped[str] = mapped_column(String(10), nullable=False)
    author:Mapped[str] = mapped_column(String(255), nullable=False)
    img_url:Mapped[str] = mapped_column(String(255))

with app.app_context():
    db.create_all()

# create a blog post creation form
class BlogForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    body = CKEditorField(label='Text', validators=[DataRequired()])
    img_url = StringField(label='Image', default='./rafa.jpg')
    submit = SubmitField(label='Post')


@app.route('/')
def home():
    blog_posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template('index.html', posts=blog_posts[:-4:-1])

@app.route('/create', methods=['GET', 'POST'])
def create_blog():
    create_form = BlogForm()
    if create_form.validate_on_submit():
        blog_post = BlogPost(
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            body=request.form.get('body'),
            img_url=request.form.get('img_url'),
            date = dt.date.today(),
            author = 'Koblih'
        )
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_blog_post.html', form=create_form)

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = BlogForm(
        title = post.title,
        subtitle = post.subtitle,
        body = post.body
    )
    if edit_form.validate_on_submit():
        blog_to_update = db.get_or_404(BlogPost, post_id)
        blog_to_update.title = request.form.get('title')
        blog_to_update.subtitle = request.form.get('subtitle')
        blog_to_update.body = request.form.get('body')
        blog_to_update.date = dt.date.today()
        db.session.commit()
        return redirect(url_for('blog_post_detail', post_id=post_id))

    return render_template('edit_blog_post.html', post=post, form=edit_form)

# TODO: delete_post() to remove a blog post from the database

@app.route('/about')
def about_author():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def blog_post_detail(post_id):
    blog_post = db.get_or_404(BlogPost, post_id)
    return render_template('post_detail.html', post=blog_post)


if __name__ == '__main__':
    app.run(debug=True)

