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


class TokenResponseDto(object):
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
        'access_token': 'str',
        'token_type': 'str',
        'expires_in': 'str',
        'refresh_token': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'scope': 'scope'
    }

    def __init__(self, access_token=None, token_type=None, expires_in=None, refresh_token=None, scope=None, _configuration=None):  # noqa: E501
        """TokenResponseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._token_type = None
        self._expires_in = None
        self._refresh_token = None
        self._scope = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if token_type is not None:
            self.token_type = token_type
        if expires_in is not None:
            self.expires_in = expires_in
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if scope is not None:
            self.scope = scope

    @property
    def access_token(self):
        """Gets the access_token of this TokenResponseDto.  # noqa: E501

        Access token bound to the scope as requested in the authorisation request and confirmed by the PSU.  # noqa: E501

        :return: The access_token of this TokenResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TokenResponseDto.

        Access token bound to the scope as requested in the authorisation request and confirmed by the PSU.  # noqa: E501

        :param access_token: The access_token of this TokenResponseDto.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def token_type(self):
        """Gets the token_type of this TokenResponseDto.  # noqa: E501

        The token type, in this case \"Bearer\" as is supported.  # noqa: E501

        :return: The token_type of this TokenResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this TokenResponseDto.

        The token type, in this case \"Bearer\" as is supported.  # noqa: E501

        :param token_type: The token_type of this TokenResponseDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Bearer"]  # noqa: E501
        if (self._configuration.client_side_validation and
                token_type not in allowed_values):
            raise ValueError(
                "Invalid value for `token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(token_type, allowed_values)
            )

        self._token_type = token_type

    @property
    def expires_in(self):
        """Gets the expires_in of this TokenResponseDto.  # noqa: E501

        The lifetime of the access token in seconds.  # noqa: E501

        :return: The expires_in of this TokenResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this TokenResponseDto.

        The lifetime of the access token in seconds.  # noqa: E501

        :param expires_in: The expires_in of this TokenResponseDto.  # noqa: E501
        :type: str
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """Gets the refresh_token of this TokenResponseDto.  # noqa: E501

        Refresh Token, which can be utilised to obtain a fresh access tokens in case the previous access token expired or was revoked. Especially useful in the context of AIS.  # noqa: E501

        :return: The refresh_token of this TokenResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this TokenResponseDto.

        Refresh Token, which can be utilised to obtain a fresh access tokens in case the previous access token expired or was revoked. Especially useful in the context of AIS.  # noqa: E501

        :param refresh_token: The refresh_token of this TokenResponseDto.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def scope(self):
        """Gets the scope of this TokenResponseDto.  # noqa: E501

        The scope of the access token.  # noqa: E501

        :return: The scope of this TokenResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this TokenResponseDto.

        The scope of the access token.  # noqa: E501

        :param scope: The scope of this TokenResponseDto.  # noqa: E501
        :type: str
        """

        self._scope = scope

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
        if issubclass(TokenResponseDto, dict):
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
        if not isinstance(other, TokenResponseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenResponseDto):
            return True

        return self.to_dict() != other.to_dict()
