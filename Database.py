from sqlalchemy import Table, Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    team = Column(String)
    password = Column(String)
    Date_of_birth = Column(String)


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    team_name = Column(String)
    members = Column(String)
    matches = Column(String)
    name_id = Column(Integer, ForeignKey('name.id'))
    name = relationship("User")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    team = Column(String)
    password = Column(String)
    date_of_birth = Column(String)

class Match(Base):
	__tablename__ = 'match'
	id = Column(Integer, primary_key=True)
	time = Column(Integer)
	location = Column(String)
	score = Column(Integer)
	game_complete = Column(Integer)
	team1_id = Column(Integer, ForeignKey('team.id'))
	team2_id = Column(Integer, ForeignKey('team.id'))
	team1 = relationship("Team", back_populates = 'matches')
	team2 = relationship("Team", back_populates = 'matches')



engine = create_engine('sqlite:///Database.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()