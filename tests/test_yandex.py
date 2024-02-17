from yandex import YaDiscAPIClient
from tokens import ya_token
import pytest


def test_yandex():
    yandex = YaDiscAPIClient(ya_token)
    response_create = yandex.make_folder('test_folder')
    yandex.remove_folder('test_folder')

    assert response_create['href'] == 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Ftest_folder'
    assert 'error' not in response_create
