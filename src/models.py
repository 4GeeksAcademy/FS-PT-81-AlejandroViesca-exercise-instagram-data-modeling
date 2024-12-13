import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    #Creamos claves foraneas
    from_id = Column(Integer, ForeignKey('users.id'))
    to_id = Column(Integer, ForeignKey('users.id'))
    #Conectamos la tabla con Post (N-N)
    user_from_id = relationship('Users', foreign_keys=[from_id], backref='Follower')
    user_to_id = relationship('Users', foreign_keys=[to_id], backref='Followed')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)  # No puede estar vacio (nullable) y debe ser unico (unique)
    password = Column(String, nullable=False)
    city = Column(String)

    
class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    #Conectamos la tabla con User (1-N)
    user = relationship('Users', backref='posts')

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    #Creamos claves foraneas
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    #Conectamos la tabla con Post (1-N)
    user = relationship('Users', backref='comments')
    post = relationship('Posts', backref='comments')


class Medias(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    src = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    #Conectamos la tabla con Post (1-N)
    post = relationship('Posts', backref='medias')


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e