from rest_framework.exceptions import ValidationError


def is_published_not_tru(bool):
    if bool == True:
        raise ValidationError('Невозможно сразу опубликовать объявление.')
