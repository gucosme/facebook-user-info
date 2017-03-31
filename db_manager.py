from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	fb_id = Column(String, primary_key=True)
	nome = Column(String)
	username = Column(String)
	genero = Column(String)

engine = create_engine('sqlite:///fb-users.db', echo=True)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

def setUser(user_dict):
	user = User(fb_id=user_dict['fb_id'], nome=user_dict['nome'], username=user_dict['username'], genero=user_dict['genero'])
	session.add(user)
	session.commit()

def getUser(id):
	user = session.query(User).filter_by(fb_id=id).first()
	print(user.nome)
