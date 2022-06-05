# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.tipo import Tipo  # noqa: F401,E501
from swagger_server import util


class Notificacion(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, notificacion_id: int=None, cliente_id: int=None, vehiculo: str=None, tipo: Tipo=None, descripcion: str=None):  # noqa: E501
        """Notificacion - a model defined in Swagger

        :param notificacion_id: The notificacion_id of this Notificacion.  # noqa: E501
        :type notificacion_id: int
        :param cliente_id: The cliente_id of this Notificacion.  # noqa: E501
        :type cliente_id: int
        :param vehiculo: The vehiculo of this Notificacion.  # noqa: E501
        :type vehiculo: str
        :param tipo: The tipo of this Notificacion.  # noqa: E501
        :type tipo: Tipo
        :param descripcion: The descripcion of this Notificacion.  # noqa: E501
        :type descripcion: str
        """
        self.swagger_types = {
            'notificacion_id': int,
            'cliente_id': int,
            'vehiculo': str,
            'tipo': Tipo,
            'descripcion': str
        }

        self.attribute_map = {
            'notificacion_id': 'notificacionId',
            'cliente_id': 'clienteId',
            'vehiculo': 'vehiculo',
            'tipo': 'tipo',
            'descripcion': 'descripcion'
        }
        self._notificacion_id = notificacion_id
        self._cliente_id = cliente_id
        self._vehiculo = vehiculo
        self._tipo = tipo
        self._descripcion = descripcion

    @classmethod
    def from_dict(cls, dikt) -> 'Notificacion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Notificacion of this Notificacion.  # noqa: E501
        :rtype: Notificacion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notificacion_id(self) -> int:
        """Gets the notificacion_id of this Notificacion.

        Id de la notificacion  # noqa: E501

        :return: The notificacion_id of this Notificacion.
        :rtype: int
        """
        return self._notificacion_id

    @notificacion_id.setter
    def notificacion_id(self, notificacion_id: int):
        """Sets the notificacion_id of this Notificacion.

        Id de la notificacion  # noqa: E501

        :param notificacion_id: The notificacion_id of this Notificacion.
        :type notificacion_id: int
        """

        self._notificacion_id = notificacion_id

    @property
    def cliente_id(self) -> int:
        """Gets the cliente_id of this Notificacion.

        Id del cliente  # noqa: E501

        :return: The cliente_id of this Notificacion.
        :rtype: int
        """
        return self._cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id: int):
        """Sets the cliente_id of this Notificacion.

        Id del cliente  # noqa: E501

        :param cliente_id: The cliente_id of this Notificacion.
        :type cliente_id: int
        """
        if cliente_id is None:
            raise ValueError("Invalid value for `cliente_id`, must not be `None`")  # noqa: E501

        self._cliente_id = cliente_id

    @property
    def vehiculo(self) -> str:
        """Gets the vehiculo of this Notificacion.

        VIN del vehículo  # noqa: E501

        :return: The vehiculo of this Notificacion.
        :rtype: str
        """
        return self._vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo: str):
        """Sets the vehiculo of this Notificacion.

        VIN del vehículo  # noqa: E501

        :param vehiculo: The vehiculo of this Notificacion.
        :type vehiculo: str
        """
        if vehiculo is None:
            raise ValueError("Invalid value for `vehiculo`, must not be `None`")  # noqa: E501

        self._vehiculo = vehiculo

    @property
    def tipo(self) -> Tipo:
        """Gets the tipo of this Notificacion.


        :return: The tipo of this Notificacion.
        :rtype: Tipo
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: Tipo):
        """Sets the tipo of this Notificacion.


        :param tipo: The tipo of this Notificacion.
        :type tipo: Tipo
        """
        if tipo is None:
            raise ValueError("Invalid value for `tipo`, must not be `None`")  # noqa: E501

        self._tipo = tipo

    @property
    def descripcion(self) -> str:
        """Gets the descripcion of this Notificacion.

        Descripción de la notificación  # noqa: E501

        :return: The descripcion of this Notificacion.
        :rtype: str
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        """Sets the descripcion of this Notificacion.

        Descripción de la notificación  # noqa: E501

        :param descripcion: The descripcion of this Notificacion.
        :type descripcion: str
        """

        self._descripcion = descripcion