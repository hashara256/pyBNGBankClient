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


class AddConsentAuthorisationResponseDto(object):
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
        'sca_status': 'str',
        'authorisation_id': 'str',
        'links': 'AddConsentAuthorisationResponseLinksDto'
    }

    attribute_map = {
        'sca_status': 'scaStatus',
        'authorisation_id': 'authorisationId',
        'links': '_links'
    }

    def __init__(self, sca_status=None, authorisation_id=None, links=None, _configuration=None):  # noqa: E501
        """AddConsentAuthorisationResponseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sca_status = None
        self._authorisation_id = None
        self._links = None
        self.discriminator = None

        if sca_status is not None:
            self.sca_status = sca_status
        if authorisation_id is not None:
            self.authorisation_id = authorisation_id
        if links is not None:
            self.links = links

    @property
    def sca_status(self):
        """Gets the sca_status of this AddConsentAuthorisationResponseDto.  # noqa: E501

        The status of the SCA method of this consent authorisation.  # noqa: E501

        :return: The sca_status of this AddConsentAuthorisationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._sca_status

    @sca_status.setter
    def sca_status(self, sca_status):
        """Sets the sca_status of this AddConsentAuthorisationResponseDto.

        The status of the SCA method of this consent authorisation.  # noqa: E501

        :param sca_status: The sca_status of this AddConsentAuthorisationResponseDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["received", "psuIdentified", "psuAuthenticated", "scaMethodSelected", "started", "finalised", "failed", "exempted", "withdrawn"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sca_status not in allowed_values):
            raise ValueError(
                "Invalid value for `sca_status` ({0}), must be one of {1}"  # noqa: E501
                .format(sca_status, allowed_values)
            )

        self._sca_status = sca_status

    @property
    def authorisation_id(self):
        """Gets the authorisation_id of this AddConsentAuthorisationResponseDto.  # noqa: E501

        Unique resource identification of the created authorisation sub-resource.  # noqa: E501

        :return: The authorisation_id of this AddConsentAuthorisationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_id

    @authorisation_id.setter
    def authorisation_id(self, authorisation_id):
        """Sets the authorisation_id of this AddConsentAuthorisationResponseDto.

        Unique resource identification of the created authorisation sub-resource.  # noqa: E501

        :param authorisation_id: The authorisation_id of this AddConsentAuthorisationResponseDto.  # noqa: E501
        :type: str
        """

        self._authorisation_id = authorisation_id

    @property
    def links(self):
        """Gets the links of this AddConsentAuthorisationResponseDto.  # noqa: E501

        This is a list of links containing possible next actions that can be performed after the this consent authorisation was created.  # noqa: E501

        :return: The links of this AddConsentAuthorisationResponseDto.  # noqa: E501
        :rtype: AddConsentAuthorisationResponseLinksDto
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AddConsentAuthorisationResponseDto.

        This is a list of links containing possible next actions that can be performed after the this consent authorisation was created.  # noqa: E501

        :param links: The links of this AddConsentAuthorisationResponseDto.  # noqa: E501
        :type: AddConsentAuthorisationResponseLinksDto
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
        if issubclass(AddConsentAuthorisationResponseDto, dict):
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
        if not isinstance(other, AddConsentAuthorisationResponseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddConsentAuthorisationResponseDto):
            return True

        return self.to_dict() != other.to_dict()
