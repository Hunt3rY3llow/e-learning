from sqlalchemy.orm import Session
from . import models, schemas

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(name=course.name, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_lessons(db: Session, course_id: int):
    return db.query(models.Lesson).filter(models.Lesson.course_id == course_id).all()

def create_lesson(db: Session, lesson: schemas.LessonCreate):
    db_lesson = models.Lesson(name=lesson.name, course_id=lesson.course_id)
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(
        lesson_id=question.lesson_id,
        type=question.type,
        content=question.content,
        options=question.options,
        correct_answers=question.correct_answers,
        score=question.score,
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question