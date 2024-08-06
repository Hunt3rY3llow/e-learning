from pydantic import BaseModel
from typing import List, Optional

class QuestionBase(BaseModel):
    lesson_id: int
    type: str
    content: str
    options: Optional[str] = None
    correct_answers: Optional[str] = None
    score: int

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

class LessonBase(BaseModel):
    course_id: int
    name: str

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int
    questions: List[Question] = []

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    lessons: List[Lesson] = []

    class Config:
        orm_mode = True