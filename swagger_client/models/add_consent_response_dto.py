# coding: utf-8

"""
    BNG Bank - XS2A Interface 1.0

    <h1>Summary</h1>  <p>The <strong>BNG Bank - XS2A Interface</strong> <em>API</em>. This API enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.</p>  <p>The possible Approaches are:</p>  <ul>     <li>Redirect SCA OAuth Approach</li>  </ul>  <h2>Some General Remarks Related to this version of the specification:</h2>  <ul>     <li>        <p><strong>This API definition is based on the Implementation Guidelines of the Berlin Group PSD2 API.</strong>It is not an replacement in any sense. The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group PSD2 API.</p>     </li>     <li>        <p><strong>This API definition contains the REST-API for requests from the TPP to the ASPSP.</strong></p>     </li>  </ul>  <h2>General Remarks on Data Types</h2>  <p>The Berlin Group definition of UTF-8 strings in context of the PSD2 API have to support at least the following characters</p>  <p>a b c d e f g h i j k l m n o p q r s t u v w x y z</p>  <p>A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</p>  <p>0 1 2 3 4 5 6 7 8 9</p>  <p>/ - ? : ( ) . , ' +</p>  <p>Space</p>  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class AddConsentResponseDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'consent_status': 'str',
        'consent_id': 'str',
        'links': 'AddConsentResponseLinksDto'
    }

    attribute_map = {
        'consent_status': 'consentStatus',
        'consent_id': 'consentId',
        'links': '_links'
    }

    def __init__(self, consent_status=None, consent_id=None, links=None, _configuration=None):  # noqa: E501
        """AddConsentResponseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consent_status = None
        self._consent_id = None
        self._links = None
        self.discriminator = None

        if consent_status is not None:
            self.consent_status = consent_status
        if consent_id is not None:
            self.consent_id = consent_id
        if links is not None:
            self.links = links

    @property
    def consent_status(self):
        """Gets the consent_status of this AddConsentResponseDto.  # noqa: E501

        The transaction status of the consent created.  # noqa: E501

        :return: The consent_status of this AddConsentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._consent_status

    @consent_status.setter
    def consent_status(self, consent_status):
        """Sets the consent_status of this AddConsentResponseDto.

        The transaction status of the consent created.  # noqa: E501

        :param consent_status: The consent_status of this AddConsentResponseDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "received", "rejected", "partiallyAuthorised", "valid", "revokedByPsu", "expired", "terminatedByTpp"]  # noqa: E501
        if (self._configuration.client_side_validation and
                consent_status not in allowed_values):
            raise ValueError(
                "Invalid value for `consent_status` ({0}), must be one of {1}"  # noqa: E501
                .format(consent_status, allowed_values)
            )

        self._consent_status = consent_status

    @property
    def consent_id(self):
        """Gets the consent_id of this AddConsentResponseDto.  # noqa: E501

        This is the identifier of the consent created. This identifier will be used later to reference this consent.  # noqa: E501

        :return: The consent_id of this AddConsentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this AddConsentResponseDto.

        This is the identifier of the consent created. This identifier will be used later to reference this consent.  # noqa: E501

        :param consent_id: The consent_id of this AddConsentResponseDto.  # noqa: E501
        :type: str
        """

        self._consent_id = consent_id

    @property
    def links(self):
        """Gets the links of this AddConsentResponseDto.  # noqa: E501

        This is a list of links containing possible next actions that can be performed after the the establishing consent request.  # noqa: E501

        :return: The links of this AddConsentResponseDto.  # noqa: E501
        :rtype: AddConsentResponseLinksDto
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AddConsentResponseDto.

        This is a list of links containing possible next actions that can be performed after the the establishing consent request.  # noqa: E501

        :param links: The links of this AddConsentResponseDto.  # noqa: E501
        :type: AddConsentResponseLinksDto
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AddConsentResponseDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddConsentResponseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddConsentResponseDto):
            return True

        return self.to_dict() != other.to_dict()