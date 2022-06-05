# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNotificacionController(BaseTestCase):
    """NotificacionController integration test stubs"""

    def test_notificacion_all_get(self):
        """Test case for notificacion_all_get

        Obtiene todas las notificaciones de un cliente
        """
        query_string = [('cliente_id', 56),
                        ('order', 'order_example'),
                        ('ordering', 'ordering_example')]
        response = self.client.open(
            '/api/v1/notificacion',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notificacion_all_options(self):
        """Test case for notificacion_all_options

        Devuelve un resumen de las peticiones HTTP permitidas.
        """
        response = self.client.open(
            '/api/v1/notificacion',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notificacion_delete(self):
        """Test case for notificacion_delete

        Elimina una notificacion.
        """
        response = self.client.open(
            '/api/v1/notificacion/{notificacionId}'.format(notificacion_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notificacion_get(self):
        """Test case for notificacion_get

        Obtiene una notificación concreta.
        """
        response = self.client.open(
            '/api/v1/notificacion/{notificacionId}'.format(notificacion_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notificacion_options(self):
        """Test case for notificacion_options

        Devuelve un resumen de las peticiones HTTP permitidas.
        """
        response = self.client.open(
            '/api/v1/notificacion/{notificacionId}'.format(notificacion_id=56),
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notificacion_post(self):
        """Test case for notificacion_post

        Crea una nueva notificación
        """
        body = None
        response = self.client.open(
            '/api/v1/notificacion',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notificacion_put(self):
        """Test case for notificacion_put

        Modifica la notificación.
        """
        body = None
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/api/v1/notificacion/{notificacionId}'.format(notificacion_id=56),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
