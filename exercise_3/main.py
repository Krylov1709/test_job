from fastapi import FastAPI
from models import PeopleModel, Session, GenderEnum

app = FastAPI(
    title='Тестовое задание ШКОЛЫ IT'
)


@app.get('/people/all/')
def get_people():
    with Session() as session:
        people = session.query(PeopleModel).all()
    return people


@app.get('/people/filter_gender/')
def get_people(gender: GenderEnum, limit: int | None = None):
    with Session() as session:
        people = session.query(PeopleModel).filter(PeopleModel.gender == gender).limit(limit).all()
    return people


@app.post('/people/')
def post_people(name: str, gender: GenderEnum):
    with Session() as session:
        new_people = PeopleModel(name=name, gender=gender)
        session.add(new_people)
        session.commit()
    return {'status': 200, 'text': 'Пользователь добавлен'}


list_people = [
    {'name': 'Bob', 'gender': 'men'},
    {'name': 'Anna', 'gender': 'women'},
    {'name': 'Mad', 'gender': 'MEN'},
    {'name': 'Kate', 'age': 30},
    {'name': 'Alex', 'gender': 'men'},
    {'name': 'Maryna', 'gender': 'women'},
]


@app.post('/list_people/')
def post_list_people():
    new_list_people = [
        people for people in list_people if 'name' and 'gender' in people and
        isinstance(people['name'], str) and people['gender'] in GenderEnum.__members__
    ]
    with Session() as session:
        for people in new_list_people:
            session.add(PeopleModel(name=people['name'], gender=people['gender']))
            session.commit()
    return {'status': 200, 'text': f'Добавлены пользователи {new_list_people}'}

