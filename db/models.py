from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(dbText, nullable=True)
    ability_score_increase = db.Column(db.JSON)
    size = db.Column(db.String(10), db.CheckConstraint("size IN ('Small', 'Medium', 'Large')"))
    speed = db.Column(db.Integer)
    traits = db.Column(db.JSON)
    languages = db.Column(db.JSON)