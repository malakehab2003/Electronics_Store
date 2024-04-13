from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# create the base model
Base = declarative_base()

# specifiy the user and the password and db name
user = 'alx'
password = 'root'
db = 'electronic-store'

# create engine and create the new session
engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db}')
sess_factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(sess_factory)
Base.metadata.create_all(engine)
session = Session
