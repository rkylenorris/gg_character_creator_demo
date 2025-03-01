from forms import CharacterForm
from db_tools import db, RaceModel, ClassModel, BackgroundModel
from character_sheet import character_creator
from dotenv import load_dotenv
import os
from flask import Flask, render_template, jsonify, request
from flask_wtf.csrf import CSRFProtect

# configure app and db
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] =  os.getenv('FLASK_SECRET_KEY') 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db.init_app(app)
csrf = CSRFProtect(app)


# define home route
@app.route('/')
def home():
    return render_template('home.html')


# define create-character route
@app.route('/create-character', methods=['GET', 'POST'])
def create_character():
    # create form and populate dropdowns
    form = CharacterForm()
    form.populate_dropdowns()
    
    if form.validate_on_submit():
        # Retrieve data from the form
        name = form.name.data
        class_name = ClassModel.query.get(form.character_class.data)
        race_name = RaceModel.query.get(form.race.data)
        background_name = BackgroundModel.query.get(form.background.data)
        appearance = form.appearance.data
        
        try:
            character = character_creator(name, class_name.name, race_name.name, background_name.name, appearance)
            return render_template('character_sheet.html', character=character)
        except Exception as e:
            error = str(e)
            return render_template('create_character.html', form=form, error=error)
    
    return render_template('create_character.html', form=form)


# define get_description route for updating description dynamically
@app.route("/get_description", methods=["POST"])
def get_description():
    data = request.json
    item_type = data.get("type")
    item_id = data.get("id")

    if item_type == "race":
        item = RaceModel.query.get(item_id)
    elif item_type == "background":
        item = BackgroundModel.query.get(item_id)
    elif item_type == "class":
        item = ClassModel.query.get(item_id)
    else:
        return jsonify({"error": "Invalid type"}), 400

    return jsonify({"description": item.description}) if item else jsonify({"error": "Not found"}), 404


# run app
if __name__ == '__main__':
    app.run(debug=True)
