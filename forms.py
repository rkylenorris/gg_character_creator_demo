from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from db_tools import RaceModel, ClassModel, BackgroundModel


class CharacterForm(FlaskForm):
    name = StringField('Character Name', validators=[DataRequired(), Length(min=2, max=50)])
    character_class = SelectField('Class', 
                               coerce=int, 
                               validators=[DataRequired()])
    race = SelectField('Race', 
                       coerce=int, 
                       validators=[DataRequired()])
    background = SelectField('Background', 
                             coerce=int, 
                             validators=[DataRequired()])
    appearance = TextAreaField('Appearance')
    submit = SubmitField('Create Character')

    def populate_dropdowns(self):
        self.race.choices = [(r.id, r.name) for r in RaceModel.query.all()]
        self.character_class = [(c.id, c.name) for c in ClassModel.query.all()]
        self.background = [(b.id, b.name) for b in BackgroundModel.query.all()]
