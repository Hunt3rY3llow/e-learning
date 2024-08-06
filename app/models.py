from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    lessons = relationship("Lesson", back_populates="course")

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="lessons")
    questions = relationship("Question", back_populates="lesson")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    lesson = relationship("Lesson", back_populates="questions")
    type = Column(String)
    content = Column(String)
    options = Column(String)
    correct_answers = Column(String)
    score = Column(Integer)