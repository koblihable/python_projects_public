from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    err = 'This field is required'

    cafe = StringField(label='Cafe name', validators=[DataRequired(message=err)])
    location_url = URLField(label='Location URL', validators=[DataRequired(message=err)])
    open_time = StringField(label='open time', validators=[DataRequired(message=err)])
    closing_time = StringField(label='closing time', validators=[DataRequired(message=err)])
    coffee_rating = SelectField(
        label='coffee rating',
        choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
        validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        label='wifi rating',
        choices=['💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'],
        validators=[DataRequired()]
    )
    power_outlet = SelectField(
        label='power outlet',
        choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        data = [
            form.cafe.data,
            form.location_url.data,
            form.open_time.data,
            form.closing_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_outlet.data
        ]
        with open('./cafe-data.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
    app.run(debug=True)
