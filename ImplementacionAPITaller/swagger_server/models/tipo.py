# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Tipo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    LLEGADA = "Llegada"
    COMIENZO_DE_EVALUACI_N = "Comienzo de Evaluación"
    COMIENZO_DE_REPARACI_N = "Comienzo de Reparación"
    IMPREVISTO_DETECTADO = "Imprevisto detectado"
    REPARACI_N_FINALIZADA = "Reparación finalizada"
    ENV_O_DE_FACTURA = "Envío de factura"
    OTRO = "Otro"
    SALIDA = "Salida"
    def __init__(self):  # noqa: E501
        """Tipo - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Tipo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tipo of this Tipo.  # noqa: E501
        :rtype: Tipo
        """
        return util.deserialize_model(dikt, cls)
