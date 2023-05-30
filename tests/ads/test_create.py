import pytest

@pytest.mark.django_db
def test_create(client, user, category):
    data = {
        'name': 'test_231111',
        'author': user.pk,
        'price': 100,
        'category': category.pk,

    }

    expected_response = {
        'id': 1,
        'is_published': False,
        'name': 'test_231111',
        'price': 100,
        'description': None,
        'image': None,
        'author': user.pk,
        'category': category.pk,
    }

    response = client.post('/ad/',
                           content_type='application/json',
                           data=data,
                           )

    assert response.status_code == 201
    assert response.data == expected_response
