from faker import Faker

import string

"""Данные для авторизации в системе"""
valid_firstname = 'Ольга'
valid_lastname = 'Орлова'
valid_email = 'orlovaov1984@yandex.ru'
valid_pass = 'jBtUU8!78pJ:UXL'
valid_phone = '+79177908841'
valid_login = 'Olga-Orlova'
valid_ls = '111111111111'
from locators import AutoPageLoc
"""Фейковые данные для авторизации в системе"""
# ввод данных на русском языке
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
#ввод данных на английском языке
fake = Faker()
fake_firstname_en = fake.first_name()
fake_lastname_en = fake.last_name()
fake_password = fake.password()
fake_email = fake.email()
fake_login = fake.user_name()
invalid_ls = '899999999999'
region = 'Башкортостан Респ'









