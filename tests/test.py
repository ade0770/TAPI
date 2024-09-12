import os
import json

# Получаем путь к текущему файлу
current_file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(current_file_path)

# List of dictionaries representing students
students = [
    {
        "student_id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "date_of_birth": "1998-05-15",
        "email": "ivan.ivanov@example.com",
        "phone_number": "+7 (123) 456-7890",
        "address": "г. Москва, ул. Пушкина, д. 10, кв. 5",
        "enrollment_year": 2017,
        "major": "Информатика",
        "course": 3,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 2,
        "first_name": "Елена",
        "last_name": "Петрова",
        "date_of_birth": "1999-08-20",
        "email": "elena.petrova@example.com",
        "phone_number": "+7 (234) 567-8901",
        "address": "г. Санкт-Петербург, ул. Ленина, д. 5, кв. 8",
        "enrollment_year": 2018,
        "major": "Экономика",
        "course": 2,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 3,
        "first_name": "Алексей",
        "last_name": "Смирнов",
        "date_of_birth": "2000-03-10",
        "email": "alexey.smirnov@example.com",
        "phone_number": "+7 (345) 678-9012",
        "address": "г. Новосибирск, ул. Гагарина, д. 15, кв. 12",
        "enrollment_year": 2019,
        "major": "История",
        "course": 1,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 4,
        "first_name": "Мария",
        "last_name": "Козлова",
        "date_of_birth": "1997-11-25",
        "email": "maria.kozlova@example.com",
        "phone_number": "+7 (456) 789-0123",
        "address": "г. Екатеринбург, ул. Пушкина, д. 20, кв. 3",
        "enrollment_year": 2016,
        "major": "История",
        "course": 4,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 5,
        "first_name": "Дмитрий",
        "last_name": "Соколов",
        "date_of_birth": "1999-04-03",
        "email": "dmitry.sokolov@example.com",
        "phone_number": "+7 (567) 890-1234",
        "address": "г. Казань, ул. Маяковского, д. 25, кв. 7",
        "enrollment_year": 2018,
        "major": "Математика",
        "course": 3,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 6,
        "first_name": "Анна",
        "last_name": "Игнатьева",
        "date_of_birth": "2001-07-18",
        "email": "anna.ignatyeva@example.com",
        "phone_number": "+7 (678) 901-2345",
        "address": "г. Волгоград, ул. Ленина, д. 30, кв. 15",
        "enrollment_year": 2020,
        "major": "Биология",
        "course": 2,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 7,
        "first_name": "Павел",
        "last_name": "Кузнецов",
        "date_of_birth": "1998-09-12",
        "email": "pavel.kuznetsov@example.com",
        "phone_number": "+7 (789) 012-3456",
        "address": "г. Ростов-на-Дону, ул. Гагарина, д. 40, кв. 22",
        "enrollment_year": 2017,
        "major": "Биология",
        "course": 4,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 8,
        "first_name": "Светлана",
        "last_name": "Морозова",
        "date_of_birth": "2000-01-30",
        "email": "svetlana.morozova@example.com",
        "phone_number": "+7 (890) 123-4567",
        "address": "г. Челябинск, ул. Кирова, д. 35, кв. 2",
        "enrollment_year": 2019,
        "major": "Психология",
        "course": 1,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 9,
        "first_name": "Константин",
        "last_name": "Федоров",
        "date_of_birth": "1997-12-05",
        "email": "konstantin.fedorov@example.com",
        "phone_number": "+7 (901) 234-5678",
        "address": "г. Уфа, ул. Советская, д. 50, кв. 10",
        "enrollment_year": 2016,
        "major": "Биология",
        "course": 4,
        "special_notes": "Без особых примет"
    },
    {
        "student_id": 10,
        "first_name": "Ольга",
        "last_name": "Никитина",
        "date_of_birth": "1999-06-20",
        "email": "olga.nikitina@example.com",
        "phone_number": "+7 (012) 345-6789",
        "address": "г. Томск, ул. Ленина, д. 60, кв. 18",
        "enrollment_year": 2018,
        "major": "Экология",
        "course": 3,
        "special_notes": "Без особых примет"
    }
]

# Convert the list of dictionaries to JSON format
json_data = json.dumps(students, indent=2)

# Создание пути к файлу внутри проекта
file_path = os.path.join(project_directory, "students.json")

# Write the JSON content to a file named students.json
with open(file_path, "w") as f:
    f.write(json_data)

print(f"JSON-файл успешно создан в {os.path.abspath(file_path)}")
#print("JSON file 'students.json' has been created successfully.")
