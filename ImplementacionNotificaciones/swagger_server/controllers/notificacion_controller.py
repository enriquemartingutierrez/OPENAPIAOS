import connexion
import six

from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def notificacion_all_get(cliente_id=None, order=None, ordering=None):  # noqa: E501
    """Obtiene todas las notificaciones de un cliente

    Si se introduce como parametro el id del cliente se obtienen las notificaciones de ese cliente, en el caso en el que no se especifique el parámetro se obtendrán todas las notificaciones. # noqa: E501

    :param cliente_id: ID de un cliente
    :type cliente_id: int
    :param order: Elige atributo para ordenar: &#x60;id&#x60; o &#x60;tipo&#x60;
    :type order: str
    :param ordering: &#x60;ASC&#x60; o &#x60;DESC&#x60;
    :type ordering: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def notificacion_all_options():  # noqa: E501
    """Devuelve un resumen de las peticiones HTTP permitidas.

    Proporciona una cabecera de tipo &#x60;Allow&#x60; que indica los métodos HTTP permitidos y separados por comas. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def notificacion_delete(notificacion_id):  # noqa: E501
    """Elimina una notificacion.

    Elimina la notificacion identificada por su identificador (notificacionId). # noqa: E501

    :param notificacion_id: ID de una notificacion
    :type notificacion_id: int

    :rtype: None
    """
    return 'do some magic!'


def notificacion_get(notificacion_id):  # noqa: E501
    """Obtiene una notificación concreta.

    Devuelve una notificación concreta identificada por su identificador (notificacionId). # noqa: E501

    :param notificacion_id: ID de una notificacion
    :type notificacion_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def notificacion_options(notificacion_id):  # noqa: E501
    """Devuelve un resumen de las peticiones HTTP permitidas.

    Proporciona una cabecera de tipo &#x60;Allow&#x60; que indica los métodos HTTP permitidos y separados por comas. # noqa: E501

    :param notificacion_id: ID de una notificacion
    :type notificacion_id: int

    :rtype: None
    """
    return 'do some magic!'


def notificacion_post(body):  # noqa: E501
    """Crea una nueva notificación

    Crea una nueva notificación para un cliente del taller introduciendo los datos siguiendo el esquema. # noqa: E501

    :param body: Datos de &#x60;Notificacion&#x60;
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def notificacion_put(body, if_match, notificacion_id):  # noqa: E501
    """Modifica la notificación.

    Cambia la información de una notificación identificada por su identificador (notificacionId) # noqa: E501

    :param body: Datos de &#x60;Notificacion&#x60;
    :type body: dict | bytes
    :param if_match: ETag del recurso que se desea modificar
    :type if_match: str
    :param notificacion_id: ID de una notificacion
    :type notificacion_id: int

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
