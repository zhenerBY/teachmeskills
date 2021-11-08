from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = 'ec2-34-197-135-44.compute-1.amazonaws.com'
USERNAME = 'emlftjtatnyzpt'
DATBASE = 'd5ps6u4quumv6b'
PORT = '5432'
PASSWORD = '0ff55cfd0fd0f6022a2e78e8b0692ee75345045a50a85b452b241c5c3b90d4a0'

engine = create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATBASE}')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Pupil(Base):
    __tablename__ = 'pupils'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', backref=backref('pupils', lazy=True))
    

    def __repr__(self) -> str:
        return f'Pupil {self.first_name} {self.last_name} {self.group}'


class Dict(Base):
    __tablename__ = 'dicts'

    id = Column(Integer, primary_key=True)
    pupil_id = Column(Integer, ForeignKey('pupils.id'), nullable=False)
    pupil = relationship('Pupil', backref=backref('dict', lazy=True, uselist=False))


    def __repr__(self) -> str:
        return f'<Dict {self.pupil.first_name} {self.pupil.last_name}>'


groups_lessons = Table('grouplessons', Base.metadata,
    Column('group_id', ForeignKey('groups.id'), primary_key=True),
    Column('lesson_id', ForeignKey('lessons.id'), primary_key=True)
)

# class GroupLesson(Base):
#     __tablename__ = 'grouplessons'

#     id = Column(Integer, primary_key=True)
#     group_id = Column(Integer, ForeignKey('groups.id'))
#     lesson_id = Column(Integer, ForeignKey('lessons.id'))
#     group = relationship("Group", back_populates="lessons")
#     lesson = relationship("Lesson", back_populates="groups")
#     date = Column(DateTime, default=datetime.now())

#     def __repr__(self) -> str:
#         return f'<GroupLesson {self.group_id} {self.lesson_id} {self.date}>'


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    lessons = relationship('Lesson', secondary=groups_lessons, back_populates='groups')

    def __repr__(self):
        return f'<Group {self.id}>'


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    groups = relationship('Group', secondary=groups_lessons, back_populates='lessons')


    def __repr__(self) -> str:
        return f'<Lesson {self.name}>'


Base.metadata.create_all(engine)
