from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database



engine = create_engine(
    f'postgresql+psycopg2://test:123456@db:5432/swordsec_challenge')

db_session = scoped_session(sessionmaker(bind=engine))


if not database_exists(engine.url):
    create_database(engine.url)


Base = declarative_base()

Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
