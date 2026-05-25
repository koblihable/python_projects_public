from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

       # {column.name: getattr(self, column.name for column in self.__table__.columns)}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random', methods=['GET'])
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    # serialize the object
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route('/search')
def search_cafe():
    location = request.args.get('loc')
    cafes = db.session.execute(db.select(Cafe).filter_by(location=location)).scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify({'Error': {
            'Not Found': 'Sorry there is no cafe at this location'
        }})

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'Success': 'Successfully added new cafe'})

@app.route('/update-price/<int:id>', methods=['GET', 'PATCH'])
def update_price(id):
    try:
        cafe_to_update = db.session.get(entity=Cafe, ident=id) # will return None if cafe_id isn't found
    except AttributeError:
        return jsonify(error={'Not Found': 'Cafe not found'}), 404
    cafe_to_update.coffee_price = request.form.get('new_price')
    db.session.commit()
    return jsonify(response={'Success': 'Price successfully updated'}), 200

@app.route('/report-closed/<int:id>', methods=['GET', 'DELETE'])
def delete_cafe(id):
    api_key = 'supersecretapikey'
    if request.args.get('api_key') == api_key:
        try:
            cafe_to_delete = db.session.get(Cafe, id)
        except AttributeError:
            return jsonify(Error={'Not Found': 'Cafe does not exist'}), 404
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={'Success': f'{cafe_to_delete.name} was successfully deleted'})
    else:
        return jsonify(error={'Access Denied': 'Action not allowed'})

if __name__ == '__main__':
    app.run(debug=True)
