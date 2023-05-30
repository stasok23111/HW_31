from datetime import date

from dateutil.relativedelta import relativedelta
from rest_framework.exceptions import ValidationError


def check_birth_date(birth_date):
    user_year = relativedelta(date.today(), birth_date).years
    if user_year < 9:
        raise ValidationError(f'Регистрация только для пользователей старше 9 лет.')


def check_email(email):
    if 'rambler.ru' in email:
        raise ValidationError('Запрешена регистрация с домена "rambler.ru"')