import time
from tqdm.auto import tqdm


def show_info_me():
    """ Показывает инфо о коллеге """
    about_me = {
        'ФИО': 'Левченко Алексей',
        'Должность': 'Ведущий исследователь данных',
        'Блок': 'Технологии',
        'Делаю': 'рекомендательные системы в HR',


    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_info_patrik():
    about_me = {
        'ФИО': 'Патрикеев Михаил Алексеевич',
        'Должность': 'Ведущий инженер по разработке',
        'Блок': 'Розничный бизнес',
        'Делаю': 'Тестирую социальные и зарплатные решения',
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_info_you_v():
    about_me = {
        'Имя': 'Валерий',
        'Город': 'Самара',
        'Должность': 'Главный специалист',
        'Блок': 'Операционный центр',
        'Занимаюсь': 'Анализом счетов по банковским картам'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

        print('_' * 30)


def show_info_zylkov():
    about_me = {
        'ФИО': 'Зыльков Павел',
        'Должность': 'Инженер по сопровождению',
        'Блок': 'Технологии',
        'Делаю': 'Социальные и зарплатные решения'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_info_me_():
    about_me = {
        'ФИО': 'Шахиев Азамат Рафикович',
        'Должность': 'Старший специалист отдела безопасности',
        'Блок': 'Сервисы',
        'Делаю': 'Сопровождение технических средств безопасности'
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def info_pro_menya():
    about_me = {
        'ФИО': 'Нетяга Светлана',
        'Должность': 'Главный аудитор',
        'Подразделение': 'Управление внутреннего аудита',
        'Делаю': 'анализ розничных некредитных операций'
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_info_me2():
    about_me = {
        'ФИО': 'Солодова Наталья',
        'Должность': 'клиентский менеджер',
        'Блок': 'ДомКлик'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def info_pro_menya_ii():
    about_me = {
        'ФИО': 'Исайкина Ирина',
        'Должность': 'Заместитель руководителя ВСП',
        'Подразделение': 'ВСП',
        'Делаю': 'занимаюсь обслуживанием клиентов и решением их проблем',
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_info_me_eb():
    about_me = {
        'ФИО': 'Евгений Бодягин',
        'Должность': 'Эксперт Центра подбора в инновационные направления бизнеса',
        'Блок': 'HR',
        'Делаю': 'Методологию подбора, в т.ч. и подбор D-people и сбор статистики по подбору'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_info_you_eg():
    about_me = {
        'ФИО': 'Евгений Головачев',
        'Город': 'Самара',
        'Должность': 'клиентский менеджер',
        'Блок': 'ДомКлик',
        'Занимаюсь': 'Помощь клиентам ипотечного кредитования'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def info_pro_menya_av():
    about_me = {
        'ФИО': 'Аня Великобратова',
        'Должность': 'КМ',
        'Подразделение': 'КИБ СРБ'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


info_list = [
    show_info_me,
    info_pro_menya,
    show_info_me_,
    show_info_me2,
    show_info_patrik,
    show_info_you_eg,
    info_pro_menya_ii,
    show_info_you_v,
    show_info_zylkov,
    show_info_me_eb,
    info_pro_menya_av

]

if __name__ == "__main__":
    for show_info in info_list:
        show_info()
        for i in tqdm(range(30)):
            time.sleep(1)

        print('Спасибо за инфо!')
        print('_' * 30)
