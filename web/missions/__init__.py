from model import UserModel
from db import db_session
from pathlib import Path
import json


path = f'{Path(__file__).resolve().parent.parent}/save'



def create_user(users):
    print("Starting user task")
    for user in users:
        new_user = UserModel(user.get('first_name'),
                             user.get('last_name'),
                             user.get('email'),
                             user.get('gender'),
                             user.get('ip_address'),
                             user.get('user_name'),
                             user.get('agent'),
                             user.get('country'))

        db_session.add(new_user)
        db_session.commit()
    db_session.close()

    print("Ending user task")


def create_file(file):
    print("Starting file task")

    users = db_session.query(UserModel).all()

    save_path = f'{path}/{file}'

    if Path(save_path).exists():
        r_file = Path(save_path)
        r_file.unlink()

    saved_list = json.dumps([user.as_dict() for user in users], indent=4)

    with open(save_path, 'w') as f:
        f.write(saved_list)
        f.close()

    print("Ending file task")
