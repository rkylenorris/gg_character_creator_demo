from character_sheet import CharacterClass, Race, Background
from app import app
from db_tools import RaceModel, BackgroundModel, ClassModel, db
from pathlib import Path
import json


def load_from_json(json_dir: str, db, app) -> None:
    """
    Load data from JSON files and populate the database.
    """
    new_models = []
    
    json_dir = Path(json_dir)
    for json_file in json_dir.glob('*.json'):
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        match json_file.stem:
            case 'classes':
                for class_data in data:
                    class_obj = CharacterClass(**class_data)
                    class_model = ClassModel(class_obj)
                    new_models.append(class_model)
            case 'backgrounds':
                for background_data in data:
                    background_obj = Background(**background_data)
                    background_model = BackgroundModel(background_obj)
                    new_models.append(background_model)
            case 'races':
                for race_data in data:
                    race_obj = Race(**race_data)
                    race_model = RaceModel(race_obj)
                    new_models.append(race_model)
            case _:
                print(f"Unknown file: {json_file.name}")
    
    with app.app_context():
        db.session.bulk_save_objects(new_models)
        db.session.commit()
        print("Database populated successfully.")
        
        
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    load_from_json('data', db, app)
    print("Database created and populated.")
    db.close()
