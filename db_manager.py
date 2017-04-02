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

	def __rep__(self):
		return self.nome

engine = create_engine('sqlite:///fb-users.db', echo=True)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

def set_user(user_dict):
	user = User(fb_id=user_dict['fb_id'], nome=user_dict['nome'], username=user_dict['username'], genero=user_dict['genero'])
	print session.add(user)
	session.commit()

def get_all_users(limit):
	if limit == '':
		users = [to_dict(user) for user in session.query(User)]
	elif(limit >= 0):
		users = [to_dict(user) for user in session.query(User).limit(limit)]

	return users

def delete_user(id):
	del_status = session.query(User).filter_by(fb_id=id).delete()
	session.commit()
	return del_status

def to_dict(db_user):
	user = {'fb_id': db_user.fb_id, 'nome': db_user.nome, 'username': db_user.username, 'genero': db_user.genero}
	return user
