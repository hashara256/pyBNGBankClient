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


class FundsConfirmationDto(object):
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
        'account': 'AccountDto',
        'instructed_amount': 'EuroAmountFieldDto'
    }

    attribute_map = {
        'account': 'account',
        'instructed_amount': 'instructedAmount'
    }

    def __init__(self, account=None, instructed_amount=None, _configuration=None):  # noqa: E501
        """FundsConfirmationDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account = None
        self._instructed_amount = None
        self.discriminator = None

        self.account = account
        self.instructed_amount = instructed_amount

    @property
    def account(self):
        """Gets the account of this FundsConfirmationDto.  # noqa: E501


        :return: The account of this FundsConfirmationDto.  # noqa: E501
        :rtype: AccountDto
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this FundsConfirmationDto.


        :param account: The account of this FundsConfirmationDto.  # noqa: E501
        :type: AccountDto
        """
        if self._configuration.client_side_validation and account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def instructed_amount(self):
        """Gets the instructed_amount of this FundsConfirmationDto.  # noqa: E501


        :return: The instructed_amount of this FundsConfirmationDto.  # noqa: E501
        :rtype: EuroAmountFieldDto
        """
        return self._instructed_amount

    @instructed_amount.setter
    def instructed_amount(self, instructed_amount):
        """Sets the instructed_amount of this FundsConfirmationDto.


        :param instructed_amount: The instructed_amount of this FundsConfirmationDto.  # noqa: E501
        :type: EuroAmountFieldDto
        """
        if self._configuration.client_side_validation and instructed_amount is None:
            raise ValueError("Invalid value for `instructed_amount`, must not be `None`")  # noqa: E501

        self._instructed_amount = instructed_amount

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
        if issubclass(FundsConfirmationDto, dict):
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
        if not isinstance(other, FundsConfirmationDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundsConfirmationDto):
            return True

        return self.to_dict() != other.to_dict()
