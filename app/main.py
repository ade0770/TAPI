from fastapi import FastAPI
from core.utils import json_to_dict_list
import os
from typing import Optional

from tests.test import students

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')

# Создаем приложение
app = FastAPI()

# Функция, возвращающая приветствие при доступе к домашней странице
@app.get("/")
def hello_message():
    return {"message": "Hello there!"}

# Функция, возвращающая список всех студентов
# @app.get("/students")
# def get_all_students(course: Optional[int]=None):
#     students = json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     else:
#         return_list = []
#         for student in students:
#             if student["course"] == course:
#                 return_list.append(student)
#         return return_list

# Функция, возвращающая список студентов по конкретному курсу
@app.get("/students/{course}")
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]

    return filtered_students

