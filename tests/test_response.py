import pytest

from django.test import TestCase, override_settings
from django.urls import reverse
from django_webtest import WebTest

from .base import TESTING_MIDDLEWARE

class TestHttpResponseWithoutUserMiddleware(WebTest):
    csrf_checks = False
    direct = reverse('direct')
    direct_params = reverse('direct-param')

    def test_middleware_simple_get_request(self):
        response = self.app.get(self.direct)

        assert response.status_code == 200

    def test_middleware_simple_post_request(self):
        response = self.app.post(self.direct_params, params={'data': 'data'})

        assert response.status_code == 200

    def test_middleware_simple_put_request(self):
        response = self.app.put(self.direct_params, params={'data': 'data'})

        assert response.status_code == 200

    def test_middleware_simple_delete_request(self):
        response = self.app.delete(self.direct_params)

        assert response.status_code == 200

    def test_middleware_simple_get_with_query_string_request(self):
        response = self.app.get(self.direct_params, params={'data': 'data'})

        assert response.status_code == 200

    def test_middleware_simple_post_with_query_string_request(self):
        response = self.app.post(f'{self.direct_params}?data=data', params={'data_json': 'data_json'})

        assert response.status_code == 200

    def test_middleware_simple_put_with_query_string_request(self):
        response = self.app.put(f'{self.direct_params}?data=data', params={'data_json': 'data_json'})

        assert response.status_code == 200

    def test_middleware_simple_delete_with_query_string_request(self):
        response = self.app.delete(self.direct_params, {'data': 'data'})

        assert response.status_code == 200


@override_settings(MIDDLEWARE=TESTING_MIDDLEWARE)
class TestResponseFunctionWithUser(WebTest):
    csrf_checks = False
    direct = reverse('drf-direct')
    direct_params = reverse('drf-direct-params')

    def test_middleware_simple_get_request(self):
        response = self.app.get(self.direct_params)

        assert response.status_code == 200

    def test_middleware_simple_post_request(self):
        response = self.app.post(self.direct_params, params={'data': 'data'})

        assert response.status_code == 200

    def test_middleware_simple_put_request(self):
        response = self.app.put(self.direct_params, params={'data': 'data'})

        assert response.status_code == 200

    def test_middleware_simple_delete_request(self):
        response = self.app.delete(self.direct_params)

        assert response.status_code == 200

    def test_middleware_simple_get_with_query_string_request(self):
        response = self.app.get(self.direct_params, {'data': 'data'})

        assert response.status_code == 200

    def test_middleware_simple_post_with_query_string_request(self):
        response = self.app.post(f'{self.direct_params}?data=data', params={'data_json': 'data_json'})

        assert response.status_code == 200

    def test_middleware_simple_put_with_query_string_request(self):
        response = self.app.put(f'{self.direct_params}?data=data', params={'data_json': 'data_json'})

        assert response.status_code == 200

    def test_middleware_simple_delete_with_query_string_request(self):
        response = self.app.delete(f'{self.direct_params}', {'data': 'data'})

        assert response.status_code == 200