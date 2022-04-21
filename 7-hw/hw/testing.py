from utils import *

# print(load_students()[1])

# title_input = input().title()
#
# for s in load_professions():
#     if s['title'] == title_input:
#         print(s['skills'])

student_skill_set = set(get_student_by_pk(4)['skills'])
required_skill_set = set(get_profession_by_title('Frontend')['skills'])
print("Required")
print(required_skill_set)
print("Student already has")
print(student_skill_set)

print("Skills he lacks list")
skills_he_lacks = required_skill_set.difference(student_skill_set)
relevant_skills = student_skill_set.intersection(required_skill_set)
print("Релевантные скиллы")
print(relevant_skills)
print(list(skills_he_lacks))
# if skills_he_lack != set():
#     print(list(skills_he_lack))
# else:
#     print("Нет недостающих навыков")

skills_he_has_list = list(student_skill_set)
skills_he_lacks_list = list(skills_he_lacks)
print("he has list")
print(skills_he_has_list)
len_req = len(required_skill_set)
len_has = len(skills_he_has_list)
len_relevant = len(student_skill_set.intersection(required_skill_set))
print("Длина релевантных скиллов")
print(len_relevant)
fit_percent = round(len_relevant / len_req * 100)
print(fit_percent)
fitness_dict = {"has": skills_he_has_list,
                "lacks": skills_he_lacks_list,
                "fit_percent": fit_percent
                }
print(fitness_dict)

print(check_fitness(1, "Backend"))
