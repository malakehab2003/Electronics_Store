from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

user = 'alx'
password = 'root'
db = 'electronic-store'

engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db}')
sess_factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(sess_factory)
Base.metadata.create_all(engine)
session = Session
