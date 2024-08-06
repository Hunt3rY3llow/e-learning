# e-learning
Proyecto de academia e-learning basico

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt

3. Ejecutar Servidor
       ```bash
      uvicorn app.main:app --reload

## RUTAS Y EJEMPLOS PARA PROBAR LOS ENDPOINT
1. Crear un Curso
Endpoint: POST /courses/

URL completa: http://127.0.0.1:8000/courses/

Body (JSON):

{
  "name": "Curso de Python",
  "description": "Un curso avanzado de Python."
}
Respuesta esperada (201 Created):

{
  "id": 1,
  "name": "Curso de Python",
  "description": "Un curso avanzado de Python.",
  "lessons": []
}

2. Obtener la Lista de Cursos
Endpoint: GET /courses/

URL completa: http://127.0.0.1:8000/courses/

Respuesta esperada (200 OK):

[
  {
    "id": 1,
    "name": "Curso de Python",
    "description": "Un curso avanzado de Python.",
    "lessons": []
  }
]
3. Obtener los Detalles de un Curso
Endpoint: GET /courses/{course_id}

URL completa: http://127.0.0.1:8000/courses/1

Respuesta esperada (200 OK):

{
  "id": 1,
  "name": "Curso de Python",
  "description": "Un curso avanzado de Python.",
  "lessons": []
}
4. Crear una Lección
Endpoint: POST /lessons/

URL completa: http://127.0.0.1:8000/lessons/

Body (JSON):

{
  "name": "Lección 1: Introducción",
  "course_id": 1
}
Respuesta esperada (201 Created):

{
  "id": 1,
  "name": "Lección 1: Introducción",
  "course_id": 1,
  "questions": []
}
5. Obtener las Lecciones de un Curso
Endpoint: GET /courses/{course_id}/lessons

URL completa: http://127.0.0.1:8000/courses/1/lessons

Respuesta esperada (200 OK):

[
  {
    "id": 1,
    "name": "Lección 1: Introducción",
    "course_id": 1,
    "questions": []
  }
]
6. Crear una Pregunta
Endpoint: POST /questions/

URL completa: http://127.0.0.1:8000/questions/

Body (JSON):

{
  "lesson_id": 1,
  "type": "multiple_choice_single_answer",
  "content": "¿Qué es Python?",
  "options": "Lenguaje de programación,Serpiente,Animal,Planeta",
  "correct_answers": "Lenguaje de programación",
  "score": 5
}
Respuesta esperada (201 Created):

json
Copiar código
{
  "id": 1,
  "lesson_id": 1,
  "type": "multiple_choice_single_answer",
  "content": "¿Qué es Python?",
  "options": "Lenguaje de programación,Serpiente,Animal,Planeta",
  "correct_answers": "Lenguaje de programación",
  "score": 5
}
7. Enviar Respuestas a una Lección
Endpoint: POST /lessons/{lesson_id}/submit

Este endpoint requiere que implementes la lógica para evaluar las respuestas del estudiante y devolver un resultado. El ejemplo asume que ya tienes esta lógica implementada.

URL completa: http://127.0.0.1:8000/lessons/1/submit

Body (JSON):

{
  "student_id": 1,
  "answers": [
    {
      "question_id": 1,
      "answer": "Lenguaje de programación"
    }
  ]
}
Respuesta esperada (200 OK):

{
  "lesson_id": 1,
  "student_id": 1,
  "correct_answers": 1,
  "total_questions": 1,
  "score": 5,
  "status": "Passed"
}
