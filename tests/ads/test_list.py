import pytest

from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads = AdFactory.create_batch(6)

    expected_response = {
        'count': 6,
        'next': None,
        'previous': None,
        'results': AdListSerializer(ads, many=True).data
    }

    response = client.get(f'/ad/')

    assert response.status_code == 200
    assert response.data == expected_response
