import pytest


from ads.serializers import AdDetailSerializer
from tests.factories import AdFactory

@pytest.mark.django_db
def test_retrieve(client, token):
    ad = AdFactory.create()

    response = client.get(f'/ad/{ad.pk}/',
                          HTTP_AUTHORIZATION='Bearer ' + token
                          )

    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data
