from utils import *

pk_student_input = int(input("Введите номер студента\n"))

student_dict = get_student_by_pk(pk_student_input)
student = student_dict['full_name']
student_skills = student_dict['skills']
print(f'Студент {student}\n'
      f'Знает: {", ".join(student_skills)}')

ask_profession = input(f"выберите специальность для оценки студента {student}\n").title()

fitness_dict = check_fitness(pk_student_input, ask_profession)

print(fitness_dict)
