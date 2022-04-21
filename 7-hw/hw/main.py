from utils import *


pk_student_input = int(input("Введите номер студента\n"))

try:
    student_dict = get_student_by_pk(pk_student_input)
except IndexError:
    print("Такого юзера нет")
    quit(0)
# student_dict = get_student_by_pk(pk_student_input)
student = student_dict['full_name']
student_skills = student_dict['skills']

print(f'Студент {student}\n'
      f'Знает: {", ".join(student_skills)}')

ask_profession = input(f"выберите специальность для оценки студента {student}\n").title()

try:
    fitness_dict = check_fitness(pk_student_input, ask_profession)
except TypeError:
    print("Такой профы нет")
    quit(0)

print(fitness_dict)
