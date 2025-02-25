from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import CharacterForm
from character_sheet import character_creator  # Your character creator function

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Replace with a secure key in production
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create-character', methods=['GET', 'POST'])
def create_character():
    form = CharacterForm()
    if form.validate_on_submit():
        # Retrieve data from the form
        name = form.name.data
        class_name = form.char_class.data
        race_name = form.race.data
        background_name = form.background.data
        appearance = form.appearance.data
        
        try:
            character = character_creator(name, class_name, race_name, background_name, appearance)
            return render_template('character_sheet.html', character=character)
        except Exception as e:
            error = str(e)
            return render_template('create_character.html', form=form, error=error)
    
    return render_template('create_character.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
