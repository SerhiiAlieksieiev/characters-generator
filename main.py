import random
from faker import Faker
import file_operations


if __name__ == '__main__':
    fake = Faker("ru_RU")
    letters_mapping = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }
    skills_list = ["Стремительный прыжок",
                   "Электрический выстрел",
                   "Ледяной удар",
                   "Стремительный удар",
                   "Кислотный взгляд",
                   "Тайный побег",
                   "Ледяной выстрел",
                   "Огненный заряд"]
    runic_skills = []
    names = [[fake.first_name_male(), fake.last_name_male()],
             [fake.first_name_female(), fake.last_name_female()]]
    questionnaires_number = 10
    min_characteristics_value = 8
    max_characteristics_value = 14

    for skill in skills_list:
        for letter in skill:
            skill = skill.replace(letter, letters_mapping[letter])
        runic_skills.append(skill)

    for questionnaire_number in range(1, questionnaires_number + 1):
        random_skill = random.sample(runic_skills, 3)
        first_skill, second_skill, third_skill = random_skill
        generated_person = random.choice(names)
        first_name, last_name = generated_person
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(min_characteristics_value, max_characteristics_value),
            "agility": random.randint(min_characteristics_value, max_characteristics_value),
            "endurance": random.randint(min_characteristics_value, max_characteristics_value),
            "intelligence": random.randint(min_characteristics_value, max_characteristics_value),
            "luck": random.randint(min_characteristics_value, max_characteristics_value),
            "skill_1": first_skill,
            "skill_2": second_skill,
            "skill_3": third_skill,
        }
        file_operations.render_template(
            "charsheet.svg", "questionnaires/questionnaire{}.svg".format(questionnaire_number), context)
