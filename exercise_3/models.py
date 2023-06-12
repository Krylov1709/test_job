import atexit
import enum
from sqlalchemy import Column, Integer, String, create_engine, Enum
from sqlalchemy.orm import declarative_base, sessionmaker

PG_DSN = 'postgresql://postgres:Rhskjd@localhost:5432/flask_app'
engine = create_engine(PG_DSN)
Base = declarative_base()


class GenderEnum(enum.Enum):
    men = 'Мужской'
    women = 'Женский'


class PeopleModel(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)


# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)
