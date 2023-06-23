from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    is_dark_theme = automation_enable_dark_theme(current_time)
    assert is_dark_theme is True


def automation_enable_dark_theme(current_time):
    if time(hour=22) <= current_time > time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    return is_dark_theme

def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = automation_enable_dark_theme_and_user_chooise(current_time,dark_theme_enabled_by_user)
    assert is_dark_theme is True


def automation_enable_dark_theme_and_user_chooise(current_time,dark_theme_enabled_by_user):
    if time(hour=22) <= current_time > time(hour=6) and dark_theme_enabled_by_user is None:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is True:
        is_dark_theme = True
    else:
        is_dark_theme = False
    return is_dark_theme


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = [i for i in users[:] for y in i.values() if y == "Olga"][0]
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = [i for i in users[:] for key, value in i.items() if key == 'age' and int(value) < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = get_name_func(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = get_name_func(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = get_name_func(find_registration_button_on_login_page,page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

def get_name_func(func_name, *func_arg):
    upp_flag = True
    new = []
    for i in str(func_name.__name__):
        if upp_flag:
            new.append(str(i).upper())
            upp_flag = False
        elif str(i) == "_":
            new.append(str(' '))
            upp_flag = True
        else:
            new.append(str(i))
    name = ''.join(new) + ' ' + '[' + ', '.join(func_arg) + ']'
    return name