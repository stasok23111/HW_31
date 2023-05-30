import pytest

@pytest.fixture
@pytest.mark.django_db
def token(client, django_user_model):
    username = 'admin'
    password = '123qwe'
    role = 'admin'

    django_user_model.objects.create(
        username=username,
        password=password,
        role=role,
    )

    response = client.post(
        '/user/token/',
        {'username': username, 'password': password, 'role': role},
        format='json'
    )

    return response.data.get('access')



@pytest.fixture
@pytest.mark.django_db
def user_access_token(client, django_user_model):
    username = 'test_username'
    password = 'test_password'
    new_user = django_user_model.objects.create(username=username, password=password, role='admin')

    response = client.post('/user/token/',
                           data={'username': username, 'password': password},
                           format='json')

    return new_user, response.data.get('access')
