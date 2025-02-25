from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CharacterForm(FlaskForm):
    name = StringField('Character Name', validators=[DataRequired()])
    char_class = SelectField('Class', 
                               choices=[
                                   ('Steam Knight', 'Steam Knight'),
                                   ('Arcane Engineer', 'Arcane Engineer'),
                                   ('Gearwright', 'Gearwright'),
                                   ('Runebound Cleric', 'Runebound Cleric'),
                                   ('Wild Warden', 'Wild Warden')
                               ], 
                               validators=[DataRequired()])
    race = SelectField('Race', 
                       choices=[
                           ('Gearborn', 'Gearborn'),
                           ('Aetherians', 'Aetherians'),
                           ('Steamforged', 'Steamforged'),
                           ('Gloomkin', 'Gloomkin'),
                           ('Emberkin', 'Emberkin'),
                           ('Skyborn', 'Skyborn')
                       ], 
                       validators=[DataRequired()])
    background = SelectField('Background', 
                             choices=[
                                 ('Clockwork Orphan', 'Clockwork Orphan'),
                                 ("Steamwright's Apprentice", "Steamwright's Apprentice"),
                                 ('Arcane Archivist', 'Arcane Archivist'),
                                 ('Guild Operative', 'Guild Operative'),
                                 ('Urban Innovator', 'Urban Innovator'),
                                 ('Ethereal Envoy', 'Ethereal Envoy'),
                                 ('Steamborne Nomad', 'Steamborne Nomad'),
                                 ('Runic Forger', 'Runic Forger')
                             ], 
                             validators=[DataRequired()])
    appearance = TextAreaField('Appearance')
    submit = SubmitField('Create Character')
